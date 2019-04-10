# All imports here is for Django to see those models and for better use experience
from pay.models.payment import Payment, PaymentAdmin, PaymentSerializer
from pay.models.detail import PaymentDetails, PaymentDetailsAdmin, PaymentDetailsSerializer
from pay.models.discount import Discount, DiscountAdmin, DiscountSerializer
from pay.models.rate import Rate, RateAdmin, RateSerializer

# Getters
from app.base.helpers import get_model as __get


@__get(model=Payment)
def get_payment(id, raise_exception=True, obj=None) -> Payment:
    return obj


@__get(model=Discount)
def get_discount(id, raise_exception=True, obj=None) -> Discount:
    return obj


@__get(model=Rate)
def get_rate(id, raise_exception=True, obj=None) -> Rate:
    return obj
