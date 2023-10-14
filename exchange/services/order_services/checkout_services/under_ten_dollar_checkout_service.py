from .checkout_service import CheckoutService
from ....repositories.order_repository import OrderRepository
from exchange.repositories.currency_repository import CurrencyRepository
from django.contrib.auth.models import User
import time
from users.models import UserBalance
from celery import shared_task


class UnderTenDollarCheckoutService(CheckoutService):

    def __init__(self, total_amount, currency_symbol):
        super().__init__()
        self.total_amount = total_amount
        self.currency_symbol = currency_symbol
        self.order_repository = OrderRepository()
        self.currency = CurrencyRepository()

    def process_order(self):
        if self.can_user_pay_order:
            under_ten_dollar_checkout_task.delay(self.total_amount, self.currency_symbol)
            order = self.order_repository.create_new_order(
                user=self.get_user(),
                currency=self.get_currency(self.currency_symbol),
                total_amount_in_usd=self.total_amount
            )
            return 'The desired currency was purchased'
        else:
            return 'charge your account first'




@shared_task
def under_ten_dollar_checkout_task(total_amount, currency_symbol):
    time.sleep(10)
