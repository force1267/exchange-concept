from enum import Enum

from utils.postgres import pool

from app.model.exceptions import LowBalance
from app.model.account import Account
from app.model.wallet import Wallet


class InvoiceStatus(Enum):
    Unknown = 0
    Pending = 1
    Success = 2
    Failed = 3
    Settled = 3

class Invoice:
    id: int
    account: Account
    wallet: Wallet
    buy: bool
    amount: int

    def __init__(
        self,
        account: Account = None,
        wallet: Wallet = None,
        buy: bool = False,
        amount: int = 0,
        status: InvoiceStatus = InvoiceStatus.Unknown
    ):
        self.account = account
        self.wallet = wallet
        self.buy = buy
        self.amount = amount
        self.status = status

    def insert(self):
        sql = """
            INSERT INTO invoice (fk_account, fk_wallet, buy, amount, status) VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            self.account.id,
            self.wallet.id,
            self.buy,
            self.amount,
            self.status.name
        )

        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, values)

    @staticmethod
    def generate_and_pay_buy_invoice(account: Account, wallet: Wallet, amount: int) -> 'Invoice':
        invoice = Invoice(account, wallet, True, amount, InvoiceStatus.Pending)

        with pool.connection() as conn:
            with conn.cursor() as cur:
                # TODO add locks
                sql = "INSERT INTO invoice (fk_account, fk_wallet, buy, amount, status) VALUES (%s, %s, %s, %s, %s) RETURNING id"
                values = (
                    invoice.account.id,
                    invoice.wallet.id,
                    invoice.buy,
                    invoice.amount,
                    invoice.status.name
                )
                cur.execute(sql, values)
                (new_invoice_id,) = cur.fetchone()
                invoice.id = new_invoice_id

                with conn.transaction():
                    sql = "SELECT balance FROM account WHERE id = %s"
                    values = (
                        invoice.account.id,
                    )
                    cur.execute(sql, values)
                    (balance,) = cur.fetchone()

                    price = invoice.wallet.crypto.price_in_cents() * amount # should use fraction units
                    if balance < price:
                        raise LowBalance() # rolls back the transaction
                    
                    new_balance = balance - price

                    sql = "SELECT balance FROM wallet WHERE id = %s"
                    values = (
                        invoice.wallet.id,
                    )
                    cur.execute(sql, values)
                    (wallet_balance,) = cur.fetchone()

                    new_wallet_balance = wallet_balance + amount

                    sql = "UPDATE account SET balance = %s WHERE id = %s"
                    values = (
                        new_balance,
                        invoice.account.id
                    )
                    cur.execute(sql, values)

                    sql = "UPDATE wallet SET balance = %s WHERE id = %s"
                    values = (
                        new_wallet_balance,
                        invoice.wallet.id
                    )
                    cur.execute(sql, values)

                    sql = "UPDATE invoice SET status = %s WHERE id = %s"
                    values = (
                        InvoiceStatus.Success.name,
                        new_invoice_id
                    )
                    cur.execute(sql, values)

        return invoice