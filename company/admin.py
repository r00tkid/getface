from django.contrib import admin
from company.models import Company, Rate, Discount, Payment

admin.site.register(Company.model, Company.admin)
admin.site.register(Discount.model, Discount.admin)
admin.site.register(Rate.model, Rate.admin)
admin.site.register(Payment.model, Payment.admin)
