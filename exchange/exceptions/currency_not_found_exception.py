
class CurrencyNotFoundError(Exception):
    def __init__(self, currency_symbol):
        self.currency_symbol = currency_symbol
        super().__init__(f"Currency not found: {currency_symbol}")