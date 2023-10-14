from celery import shared_task
import time
from celery import shared_task
from abantether.celery import app


class BuyCurrencyService:

    @staticmethod
    @app.task
    def buy_from_exchange(currency_symbol, amount):
        time.sleep(10)
        print(f"Buying {amount} units of {currency_symbol} from the exchange.")
