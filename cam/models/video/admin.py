from django.contrib.admin import ModelAdmin as _Admin


class VideoAdmin(_Admin):
    list_display = ("id", "filename", "start", "duration", "camera", "timezone")
