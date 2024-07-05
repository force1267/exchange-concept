import os


POSTGRES_ADDRESS = os.environ.get('POSTGRES_ADDRESS', 'postgres://postgres:12345678@postgres:5432/exchange')
