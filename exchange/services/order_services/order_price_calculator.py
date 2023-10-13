from exchange.repositories.currency_repository import CurrencyRepository


class OrderPriceCalculator:
    def __init__(self):
        self.currency_repository = CurrencyRepository()

    def calculate_price(self, currency_symbol, amount):
        currency_price = self.currency_repository.get_currency_price_with_symbol(currency_symbol)
        return currency_price * amount
