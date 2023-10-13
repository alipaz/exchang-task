from rest_framework import serializers
from ..repositories.currency_repository import CurrencyRepository


class OrderRequestValidation(serializers.Serializer):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.currency_repository = CurrencyRepository()

    amount = serializers.DecimalField(
        max_digits=10,
        decimal_places=6,
        error_messages={
            'max_digits': 'The amount field must have a maximum of 10 digits.',
            'max_decimal_places': 'The amount field must have a maximum of 6 decimal places.',
        },
        required=True
    )
    currency_symbol = serializers.CharField(
        max_length=20,
        error_messages={
            'max_length': 'The currency_symbol must be uppercase and have a maximum length of 20 characters.',
        },
        required=True
    )

    def check_is_currency_exist(self, currency_symbol):
        test = self.currency_repository.get_single_currency('ETH')
        print('test')

    # def validate(self, data):
    #     self.check_user_balance()
    #     self.check_is_currency_exist()
    #     return data

    # def check_user_balance(self):
    #     test = self.currency_repository.get_all_currency
    #     print(test)
