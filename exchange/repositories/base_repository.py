from ..models import BaseModel
import os
from django.core.cache import cache
import redis


class BaseRepository:
    def __init__(self):
        self.model = BaseModel

    SHORT_CACHE_TTL = 3600  # 1 Hour
    MID_CACHE_TTL = 86400  # 1 Day
    LONG_CACHE_TTL = 2592000  # 1 Week

    def get_cache_key_prefix(self, model: object):
        return f"{self.get_app_name_connection()}:{model._meta.model_name}"

    def get_app_name_connection(self):
        return 'exchange'

    @staticmethod
    def clear_cache():
        cache.clear()
