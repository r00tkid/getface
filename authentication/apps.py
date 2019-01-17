from django.apps import AppConfig
from django.utils.html import format_html


class AuthenticationConfig(AppConfig):
    name = 'authentication'
    verbose_name = format_html("Авторизация <i class='fa fa-user-circle' aria-hidden='true'></i>")
