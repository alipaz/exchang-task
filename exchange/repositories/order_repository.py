from .base_repository import BaseRepository
from ..models.order import Order
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist


class OrderRepository(BaseRepository):

    def __init__(self):
        super().__init__()
        self.order = Order

    def get_cache_key(self, order_id):
        return f"{self.get_cache_key_prefix(model=self.order)}:{order_id}"

    def create_new_order(self, user, currency, total_amount_in_usd, status='pending', completed_at=None):
        new_order = self.order.objects.create(
            user=user,
            currency=currency,
            total_amount_in_usd=total_amount_in_usd,
            completed_at=completed_at,
            status=status
        )

        if status == 'pending' and total_amount_in_usd < 10:
            cache_key = self.get_cache_key("under_10_usd_pending_orders")
            under_10_usd_orders = cache.get(cache_key, [])

            under_10_usd_orders.append(new_order)
            cache.set(cache_key, under_10_usd_orders)

        return new_order

    def get_order_by_id(self, order_id):
        cache_key = self.get_cache_key(order_id)
        order = cache.get(cache_key)

        if order is not None:
            return order
        try:
            order = self.order.objects.get(id=order_id)
            cache.set(cache_key, order)
            return order
        except ObjectDoesNotExist:
            return "Order not found."

    def update_order_status(self, order_id, status, completed_at=None):
        try:
            order = self.order.objects.get(id=order_id)
        except ObjectDoesNotExist:
            return "Order not found."

        if order.status != 'completed' and status == 'completed':
            # Remove the order from the "under_10_usd_pending_orders" cache list
            under_10_usd_cache_key = self.get_cache_key("under_10_usd_pending_orders")
            under_10_usd_orders = cache.get(under_10_usd_cache_key, [])
            under_10_usd_orders = [o for o in under_10_usd_orders if o.id != order.id]
            cache.set(under_10_usd_cache_key, under_10_usd_orders)

        order.status = status
        order.completed_at = completed_at
        order.save()

        if status == 'completed':
            # Delete the order-specific cache key
            cache_key = self.get_cache_key(order_id)
            cache.delete(cache_key)

        return order

    def get_under_ten_dollar_pending_orders(self):
        cache_key = self.get_cache_key("under_10_usd_pending_orders")
        under_10_usd_orders = cache.get(cache_key)

        if under_10_usd_orders is not None:
            return under_10_usd_orders

        pending_orders = self.order.objects.filter(status='pending', total_amount_in_usd__lt=10)
        under_10_usd_orders = list(pending_orders)
        cache.set(cache_key, under_10_usd_orders)

        return under_10_usd_orders



