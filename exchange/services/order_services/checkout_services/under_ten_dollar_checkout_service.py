from .checkout_service import CheckoutService
from ....repositories.order_repository import OrderRepository
from exchange.repositories.currency_repository import CurrencyRepository
from django.contrib.auth.models import User
import time
from django.utils import timezone
from abantether.celery import app
from celery import shared_task


class UnderTenDollarCheckoutService(CheckoutService):

    def __init__(self, total_amount, currency_symbol):
        self.total_amount = total_amount
        self.currency_symbol = currency_symbol
        self.order_repository = OrderRepository()
        self.currency = CurrencyRepository()

    def process_order(self):
        under_ten_dollar_checkout_task.delay(self.total_amount, self.currency_symbol)
        order = self.order_repository.create_new_order(
            user=self.get_user(),
            currency=self.currency.get_currency_by_symbol(self.currency_symbol),
            total_amount_in_usd=self.total_amount
        )
        # orders = self.order_repository.get_under_ten_dollar_pending_orders()
        # for test in orders:
        #     print(orders)
        #     self.order_repository.update_order_status(test.id, 'completed', timezone.now())
        #     print(test.total_amount_in_usd)

    def get_user(self):
        return User.objects.get(id=1)


@shared_task
def under_ten_dollar_checkout_task(total_amount, currency_symbol):
    time.sleep(10)
