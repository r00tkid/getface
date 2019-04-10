from django.contrib.admin import ModelAdmin as _Admin


class ScheduleAdmin(_Admin):
    list_display = (
        'employee_fullname',
        'company_name',
        'start',
        'end',
        'is_wanted',
        'timezone',
    )
