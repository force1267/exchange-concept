from typing import Tuple

from app.controller.exceptions import CryptoNotSupported, DBError, LowBalance
from app.controller.foreign_exchange import buy_from_exchange

from app.model.crypto import Crypto
from app.model.account import Account
from app.model.wallet import Wallet
from app.model.invoice import Invoice, InvoiceStatus

from config.exchage import EXCHANGE_MIN_TRANSACTION_CENTS


def buy(user, crypto, amount) -> dict:
    if not Crypto.is_supported(crypto):
        raise CryptoNotSupported
    
    try:
        accounts = Account.get_user_accounts(user)
    except Exception as e:
        raise DBError(e)

    # create initial account for simplicity
    if len(accounts) == 0:
        try:
            account = Account.create_account_for_user(user, 1000)
        except Exception as e:
            raise DBError(e)
    else:
        account = accounts[0]

    try:
        wallet = Wallet.get_or_create_user_wallet(user, crypto)
    except Exception as e:
        raise DBError(e)

    try:
        invoice, price = Invoice.generate_and_pay_buy_invoice(account, wallet, amount)
    except LowBalance as e:
        raise e
    except Exception as e:
        raise DBError(e)

    # here can use something like celery
    # we can also let the buy happen with cronjob
    if price > EXCHANGE_MIN_TRANSACTION_CENTS:
        invoice.update_status(InvoiceStatus.Settling)
        buy_from_exchange(crypto, amount)
        invoice.update_status(InvoiceStatus.Settled)

    return {
        'invoice': invoice.id,
        'account': invoice.account.id,
        'wallet': invoice.wallet.id,
    }