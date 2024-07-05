
class LowBalance(Exception):
    def __init__(self):
        super().__init__('balance is low')
