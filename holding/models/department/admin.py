from django.contrib.admin import ModelAdmin as _Admin


class CompanyAdmin(_Admin):
    list_display = ('name', 'company', 'id',)
