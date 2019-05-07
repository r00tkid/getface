from django.utils.html import format_html
from django.apps import AppConfig


class CommonConfig(AppConfig):
    name = 'common'
    verbose_name = format_html("Общее <i class='fa fa-globe' aria-hidden='true'></i>")
