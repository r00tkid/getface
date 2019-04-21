from django.contrib.admin import ModelAdmin as _Admin


class CompanyAdmin(_Admin):
    list_display = ('name', 'created_at', 'timezone', 'time_left', 'rate', 'employee_amount', 'departments_amount', 'id',)
