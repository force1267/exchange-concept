from app.model.exceptions import LowBalance

class CryptoNotSupported(Exception):
    def __init__(self):
        super().__init__('crypto not supported')

class DBError(Exception):
    def __init__(self, exception: Exception):
        super().__init__(exception)
