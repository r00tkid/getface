from django.contrib.admin import ModelAdmin as _Admin


class DiscountAdmin(_Admin):
    list_display = ('name', 'percent')
