from django.contrib import admin
from company.models import Company, Worker

admin.site.register(Company.model(), Company.admin_view())
admin.site.register(Worker.model(), Worker.admin_view())
