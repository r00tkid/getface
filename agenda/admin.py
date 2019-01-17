from django.contrib import admin
from agenda import models

admin.site.register(models.WorkerAgenda)
admin.site.register(models.WorkerFaceTime)
