from .checkout_service import CheckoutService
from exchange.services.order_services.buy_currency_service import BuyCurrencyService
from ....repositories.order_repository import OrderRepository


class HigherTenDollarCheckoutService(CheckoutService):

    def __init__(self, total_amount, currency_symbol):
        super().__init__()
        self.total_amount = total_amount
        self.currency_symbol = currency_symbol
        self.buy_currency_service = BuyCurrencyService()
        self.order_repository = OrderRepository()

    def process_order(self):
        if self.get_user_balance:
            order = self.order_repository.create_new_order(
                user=self.get_user(),
                currency=self.get_currency(self.currency_symbol),
                total_amount_in_usd=self.total_amount
            )

            self.buy_currency_service.buy_from_exchange.delay(self.currency_symbol, self.total_amount)

            return 'The desired currency was purchased'
        else:
            return 'charge your account first'


