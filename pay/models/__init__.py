# All imports here is for Django to see those models and for better use experience
from pay.models.payment import Payment, PaymentAdmin, PaymentSerializer
from pay.models.detail import PaymentDetails, PaymentDetailsAdmin, PaymentDetailsSerializer
from pay.models.discount import Discount, DiscountAdmin, DiscountSerializer
from pay.models.rate import Rate, RateAdmin, RateSerializer
