from django.db import models
from .base_model import BaseModel


class Currency(BaseModel):
    symbol = models.CharField(max_length=20, db_index=True)
    price_in_usd = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.symbol
