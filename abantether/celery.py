from __future__ import absolute_import, unicode_literals
from celery import Celery
from django.conf import settings
import os

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abantether.settings')

# Create a Celery instance.
app = Celery('abantether')

# Configure Celery using Django settings.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover and register Celery tasks from your Django app.
app.autodiscover_tasks()

# Define the Celery beat schedule.
app.conf.beat_schedule = {
    'check_pending_under_10_dollar_order': {
        'task': 'exchange.tasks.check_under_ten_dollar_order',
        'schedule': 1,
        'options': {
            'expire': 10
        }
    }
}
