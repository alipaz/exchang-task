from abc import ABC, abstractmethod


class CheckoutService(ABC):
    @abstractmethod
    def process_order(self):
        pass

    def buy_from_exchange(self, currency_symbol, amount):
        pass

    def can_user_pay_order(self):
        pass
