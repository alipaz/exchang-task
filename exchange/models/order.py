from django.db import models
from .base_model import BaseModel
from django.contrib.auth.models import User
from .currency import Currency


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    total_amount_in_usd = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    completed_at = models.DateTimeField(null=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"
