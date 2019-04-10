from django.contrib import admin
from .models import Logbook, LogbookAdmin, Schedule, ScheduleAdmin, Violation, ViolationAdmin

admin.site.register(Logbook, LogbookAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Violation, ViolationAdmin)
