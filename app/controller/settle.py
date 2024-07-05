
from config.exchage import EXCHANGE_MIN_TRANSACTION_CENTS

from app.controller.foreign_exchange import buy_from_exchange

from app.model.invoice import Invoice, SettleCallbackError
from app.model.crypto import crypto_name_to_class

def settle_callback(groups) -> bool:
    for group in groups:
        crypto_name = group[0]
        amount = group[1]
        price_per_token = crypto_name_to_class[crypto_name].price_in_cents()
        total = price_per_token * amount
        if total < EXCHANGE_MIN_TRANSACTION_CENTS:
            return False

    for group in groups:
        crypto_name = group[0]
        amount = group[1]
        buy_from_exchange(crypto_name, amount)

    return True

def settle():
    try:
        Invoice.settle_invoices(settle_callback)
    except SettleCallbackError as e:
        print('failed to buy from foreign exchange')
    except Exception as e:
        raise e
