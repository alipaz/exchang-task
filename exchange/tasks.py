from celery import shared_task
from exchange.repositories.order_repository import OrderRepository
from django.utils import timezone
from exchange.repositories.currency_repository import CurrencyRepository


@shared_task
def check_under_ten_dollar_order():
    currencies = CurrencyRepository().get_all_currency
    order_repository = OrderRepository()
    orders = order_repository.get_under_ten_dollar_pending_orders()

    orders_total_amount_in_dollar = 0
    selected_orders = []

    for order in orders:
        # i need fix this to only orders with same currency_id
        orders_total_amount_in_dollar += order.total_amount_in_usd
        selected_orders.append(order)

        if orders_total_amount_in_dollar >= 10:
            buy_from_exchange()

            for sent_order in selected_orders:
                repository = OrderRepository()
                repository.update_order_status(order_id=sent_order.id, status='completed', completed_at=timezone.now())

def buy_from_exchange():
    print('Buying from the exchange when total amount is at least $10')
