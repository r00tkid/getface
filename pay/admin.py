from django.contrib import admin
from .models import Payment, PaymentAdmin, PaymentDetails, PaymentDetailsAdmin, Discount, DiscountAdmin, Rate, RateAdmin

admin.site.register(Payment, PaymentAdmin)
admin.site.register(PaymentDetails, PaymentDetailsAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Rate, RateAdmin)
