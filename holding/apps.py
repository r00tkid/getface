from django.utils.html import format_html
from django.apps import AppConfig


class HoldingConfig(AppConfig):
    name = 'holding'
    verbose_name = format_html("Предприятия <i class='fa fa-building-o' aria-hidden='true'></i>")
