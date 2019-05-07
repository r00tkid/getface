from django.urls import path, include
from .views import payment, rate

urlpatterns = [
    path('/rate/available', rate.available),
    path('/rate/buy', payment.buy_rate),
]
