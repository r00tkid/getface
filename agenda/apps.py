from django.apps import AppConfig
from django.utils.html import format_html


class AgendaConfig(AppConfig):
    name = 'agenda'
    verbose_name = format_html("Расписание <i class='fa fa-calendar' aria-hidden='true'></i>")
