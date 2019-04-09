from django.utils.html import format_html
from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    name = 'auth'
    verbose_name = format_html("Авторизация <i class='fa fa-user-circle' aria-hidden='true'></i>")
