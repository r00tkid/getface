from django.contrib.admin import ModelAdmin as _Admin


class CameraAdmin(_Admin):
    list_display = ("name", "ip_address", "is_active", "company", "zone", "timezone")
