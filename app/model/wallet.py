from typing import Type, List

from utils.postgres import pool

from app.model.crypto import Crypto, USDT, crypto_name_to_class


class Wallet:
    id: int
    user_id: int
    crypto: Type[Crypto]
    balance: int
    def __init__(
        self,
        id: int = 0,
        user_id: int = 0,
        crypto: Type[Crypto] = USDT,
        balance: int = 0
    ):
        self.id = id
        self.user_id = user_id
        self.crypto = crypto
        self.balance = balance

    @staticmethod
    def get_user_wallet(user_id: int, crypto: str) -> List['Wallet']:
        sql = """
            SELECT id, balance FROM wallet WHERE user_id = %s AND crypto = %s
        """
        values = (
            user_id,
            crypto
        )

        walls = None
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, values)
                walls = cur.fetchall()

        return [Wallet(w[0], user_id, crypto_name_to_class[crypto], w[1]) for w in walls]


    @staticmethod
    def get_or_create_user_wallet(user_id: int, crypto: str) -> 'Wallet':
        walls = Wallet.get_user_wallet(user_id, crypto)
        if len(walls) > 0:
            return walls[0]

        sql = """
            INSERT INTO wallet (user_id, crypto, balance) VALUES (%s, %s, %s)
        """
        values = (
            user_id,
            crypto,
            0
        )

        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, values)

        return Wallet.get_user_wallet(user_id, crypto)[0]