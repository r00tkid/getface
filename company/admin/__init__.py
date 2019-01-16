from django.contrib import admin
from company.models import Company, Worker
from . import models

admin.site.register(Company)
admin.site.register(Worker, models.WorkerAdmin)
