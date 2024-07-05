
from utils.postgres import pool


class Account:
    id: int
    user_id: int
    balance_in_cents: int

    def __init__(
        self,
        id: int = 0,
        user_id: int = 0,
        balance_in_cents: int = 0
    ):
        self.id = id
        self.user_id = user_id
        self.balance_in_cents = balance_in_cents

    @staticmethod
    def get_user_accounts(user_id: int):
        sql = """
            SELECT id, balance FROM account WHERE user_id = %s
        """
        values = (
            user_id,
        )

        accs = None
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, values)
                accs = cur.fetchall()

        return [Account(a[0], user_id, a[1]) for a in accs]

    @staticmethod
    def create_account_for_user(user_id: int, initial_balance: int) -> 'Account':
        sql = """
            INSERT INTO account (user_id, balance) VALUES (%s, %s)
        """
        values = (
            user_id,
            initial_balance
        )

        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, values)

        return Account.get_user_accounts(user_id)[0]
