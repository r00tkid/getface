from django.apps import AppConfig
from django.utils.html import format_html


class CompanyConfig(AppConfig):
    name = 'company'
    verbose_name = format_html("Предприятия <i class='fa fa-building-o' aria-hidden='true'></i>")
