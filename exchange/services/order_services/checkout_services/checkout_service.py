from abc import ABC, abstractmethod
from users.repositories.user_repository import UserRepository
from users.repositories.user_balance_repository import UserBalanceRepository
from exchange.repositories.currency_repository import CurrencyRepository


class CheckoutService(ABC):
    def __init__(self):
        self.user_repository = UserRepository()
        self.user_balance_repository = UserBalanceRepository()
        self.currency_repository = CurrencyRepository()

    @abstractmethod
    def process_order(self):
        pass

    def get_user_balance(self):
        return self.user_balance_repository.get_user_balance_with_user_id()

    def get_user(self):
        # Hard-coded user ID
        return self.user_repository.get_user_by_id()

    def get_currency(self, symbol: str):
        return self.currency_repository.get_currency_by_symbol(symbol)

    def can_user_pay_order(self, total_amount) -> bool:
        user_balance = self.get_user_balance()
        return user_balance >= total_amount
