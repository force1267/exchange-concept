
class LowBalance(Exception):
    def __init__(self):
        super().__init__('balance is low')

class InvalidQuery(Exception):
    def __init__(self, msg):
        super().__init__('invalid query: ' + msg)

class SettleCallbackError(Exception):
    def __init__(self):
        super().__init__('provided callback did not work')
