from django.contrib import admin
from company.models import Company, Worker, Rate, Discount, Payment, Department, Position

admin.site.register(Company.model(), Company.admin_view())
admin.site.register(Discount.model(), Discount.admin_view())
admin.site.register(Rate.model(), Rate.admin_view())
admin.site.register(Payment.model(), Payment.admin_view())

admin.site.register(Worker.model(), Worker.admin_view())
admin.site.register(Department.model())
admin.site.register(Position.model())
