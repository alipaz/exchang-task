from users.models import UserBalance


class UserBalanceRepository:
    def __init__(self):
        self.user_balance = UserBalance()

    def get_user_balance_with_user_id(self, user_id=1):
        return self.user_balance.objects.get(id=user_id)
