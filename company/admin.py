from django.contrib import admin
from company.models import Company, Rate, Discount, Payment

admin.site.register(Company.model(), Company.admin_view())
admin.site.register(Discount.model(), Discount.admin_view())
admin.site.register(Rate.model(), Rate.admin_view())
admin.site.register(Payment.model(), Payment.admin_view())
