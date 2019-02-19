from django.apps import AppConfig
from django.utils.html import format_html


class EmployeeConfig(AppConfig):
    name = 'employee'
    verbose_name = format_html("Штат <i class='fa fa-user-circle' aria-hidden='true'></i>")
