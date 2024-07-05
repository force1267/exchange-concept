
from abc import ABC, abstractmethod
from typing import Type, List, Dict


class Crypto(ABC):
    @classmethod
    @abstractmethod
    def symbol(cls) -> str:
        pass

    @classmethod
    @abstractmethod
    def price_in_cents(cls) -> int:
        pass
    
    @staticmethod
    def is_supported(crypto: str) -> bool:
        if crypto in [c.symbol() for c in [
            ABAN,
            USDT,
            BTC
        ]]:
            return True
        return False

    @staticmethod
    def get_crypto_class(crypto: str) -> Type['Crypto']:
        return crypto_name_to_class[crypto]

class ABAN(Crypto):
    def __init__(self):
        pass

    @classmethod
    def symbol(cls):
        return "ABAN"

    @classmethod
    def price_in_cents(cls):
        return 400 # hard coded for simplicity

class USDT(Crypto):
    def __init__(self):
        pass

    @classmethod
    def symbol(cls):
        return "USDT"

    @classmethod
    def price_in_cents(cls):
        return 12

class BTC(Crypto):
    def __init__(self):
        pass

    @classmethod
    def symbol(cls):
        return "BTC"

    @classmethod
    def price_in_cents(cls):
        return 12




crypto_list: List[Type[Crypto]] = [
    ABAN,
    USDT,
    BTC
]

crypto_name_to_class: Dict[str, Type[Crypto]] = {class_object.symbol(): class_object for class_object in crypto_list}
