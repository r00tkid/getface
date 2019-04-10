from django.contrib.admin import ModelAdmin as _Admin


class DepartmentAdmin(_Admin):
    list_display = ('name', 'company', 'id',)
