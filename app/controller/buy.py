from typing import Tuple

from app.controller.exceptions import CryptoNotSupported, DBError, LowBalance

from app.model.crypto import Crypto
from app.model.account import Account
from app.model.wallet import Wallet
from app.model.invoice import Invoice

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
        invoice = Invoice.generate_and_pay_buy_invoice(account, wallet, amount)
    except LowBalance as e:
        raise e
    except Exception as e:
        raise DBError(e)

    
    return {
        'invoice': invoice.id,
        'account': invoice.account.id,
        'wallet': invoice.wallet.id,
    }