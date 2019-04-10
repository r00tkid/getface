from django.contrib.admin import ModelAdmin as _Admin


class ViolationAdmin(_Admin):
    list_display = (
        'employee_fullname',
        'when',
        'title',
        'timezone',
    )
