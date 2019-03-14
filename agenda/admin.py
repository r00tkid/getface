from django.contrib import admin
from agenda.models import Agenda, Calendar

admin.site.register(Agenda.model, Agenda.admin)
admin.site.register(Calendar.model, Calendar.admin)
