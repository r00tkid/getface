from django.contrib.admin import ModelAdmin as _Admin


class LogbookAdmin(_Admin):
    list_display = (
        'employee_fullname',
        'company_name',
        'start',
        'end',
        'activity',
        'mood',
        'fatigue',
        'timezone',
    )
