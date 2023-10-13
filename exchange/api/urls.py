from django.urls import path
from ..views.order_view import OrderView

urlpatterns = [
    path('/order', OrderView.as_view()),
]