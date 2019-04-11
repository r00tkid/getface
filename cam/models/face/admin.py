from django.contrib.admin import ModelAdmin as _Admin


class FaceAdmin(_Admin):
    list_display = ('employee', 'face_id', 'id')
