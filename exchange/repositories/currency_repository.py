from .base_repository import BaseRepository
from ..models import Currency
from django.core.cache import cache
from exchange.exceptions.currency_not_found_exception import CurrencyNotFoundError


class CurrencyRepository(BaseRepository):

    def __init__(self):
        super().__init__()
        self.currency = Currency

    def get_all_currency(self):
        cache_key = self.get_cache_key_prefix(model=self.currency) + ':all_currencies'
        # cache_key = exchange:currency:all_currencies
        currency_data = cache.get(cache_key)

        if currency_data is None:
            currency_data = self.currency.objects.values('symbol', 'price_in_usd')

            currency_dict = {entry['symbol']: entry['price_in_usd'] for entry in currency_data}

            cache.set(cache_key, currency_dict, self.MID_CACHE_TTL)
            # example = {'ETH': Decimal('2000.00'), 'BSC': Decimal('500.00')}
        return currency_data

    def get_currency_price_with_symbol(self, currency_symbol):
        all_currencies = self.get_all_currency()

        if all_currencies is not None:
            return all_currencies.get(currency_symbol)

        try:
            currency_data = self.currency.objects.get(symbol=currency_symbol)
            return currency_data.price_in_usd
        except self.currency.DoesNotExist:
            return None

    def get_currency_by_symbol(self, currency_symbol):
        try:
            return self.currency.objects.get(symbol=currency_symbol)
        except self.currency.DoesNotExist:
            raise CurrencyNotFoundError(currency_symbol)