from celery import shared_task
import time


class BuyCurrencyService:

    @staticmethod
    @shared_task
    def buy_from_exchange(currency_symbol, amount):
        time.sleep(10)
        print(f"Buying {amount} units of {currency_symbol} from the exchange.")
