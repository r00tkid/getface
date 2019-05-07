from django.contrib.admin import ModelAdmin as _Admin


class PaymentAdmin(_Admin):
    list_display = ('company', 'user', 'rate', 'discount',)
