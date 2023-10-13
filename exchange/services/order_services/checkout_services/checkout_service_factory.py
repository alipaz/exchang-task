from .higher_ten_dollar_checkout_service import HigherTenDollarCheckoutService
from .under_ten_dollar_checkout_service import UnderTenDollarCheckoutService


class CheckoutServiceFactory:

    def create_checkout_service(self, total_amount, currency_symbol):
        if total_amount < 10:
            return UnderTenDollarCheckoutService(total_amount, currency_symbol)
        else:
            return HigherTenDollarCheckoutService(total_amount, currency_symbol)
