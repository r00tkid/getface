from django.contrib.admin import ModelAdmin as _Admin


class ZoneAdmin(_Admin):
    list_display = ('company', 'name',)
