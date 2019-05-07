from django.utils.html import format_html
from django.apps import AppConfig


class PaymentConfig(AppConfig):
    name = 'pay'
    verbose_name = format_html("Платежи <i class='fa fa-money' aria-hidden='true'></i>")
