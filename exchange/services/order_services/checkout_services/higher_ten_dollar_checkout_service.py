from .checkout_service import CheckoutService


class HigherTenDollarCheckoutService(CheckoutService):

    def __init__(self, total_amount, currency_symbol):
        self.total_amount = total_amount
        self.currency_symbol = currency_symbol

    def process_order(self):
        return f"Processing checkout for orders over $10 with a total of ${self.total_amount} in {self.currency_symbol}"
