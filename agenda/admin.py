from django.contrib import admin
from agenda.models import Agenda, Calendar

admin.site.register(Agenda.model(), Agenda.admin_view())
admin.site.register(Calendar.model(), Calendar.admin_view())
