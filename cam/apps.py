from django.utils.html import format_html
from django.apps import AppConfig


class CameraConfig(AppConfig):
    name = 'cam'
    verbose_name = format_html("Видео <i class='fa fa-camera' aria-hidden='true'></i>")
