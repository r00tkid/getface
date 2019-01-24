from django.contrib import admin
from company.models import Company, Worker, Discount

admin.site.register(Company.model(), Company.admin_view())
admin.site.register(Worker.model(), Worker.admin_view())
admin.site.register(Discount.model(), Discount.admin_view())
