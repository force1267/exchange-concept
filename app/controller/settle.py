
from config.exchage import EXCHANGE_MIN_TRANSACTION_CENTS

from app.controller.foreign_exchange import buy_from_exchange

from app.model.invoice import Invoice, SettleCallbackError

def settle_callback(groups) -> bool:
    for group in groups:
        if group[1] < EXCHANGE_MIN_TRANSACTION_CENTS:
            return False

    for group in groups:
        buy_from_exchange(group[0], group[1])

    return True

def settle():
    try:
        Invoice.settle_invoices(settle_callback)
    except SettleCallbackError as e:
        print('failed to buy from foreign exchange')
    except Exception as e:
        raise e