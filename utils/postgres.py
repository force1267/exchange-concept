from psycopg_pool import ConnectionPool

from config.postgres import POSTGRES_ADDRESS


pool = ConnectionPool(POSTGRES_ADDRESS, open=True)
