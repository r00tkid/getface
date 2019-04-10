from django.utils.html import format_html
from django.apps import AppConfig


class JobConfig(AppConfig):
    name = 'job'
    verbose_name = format_html("Календари <i class='fa fa-briefcase' aria-hidden='true'></i>")
