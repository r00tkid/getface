from django.contrib.admin import ModelAdmin as _Admin


class RateAdmin(_Admin):
    list_display = ('name', 'per_month', 'is_archived', 'id')
