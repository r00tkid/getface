from django.contrib import admin
from .models import Camera, CameraAdmin, Face, FaceAdmin, Video, VideoAdmin, Zone, ZoneAdmin

admin.site.register(Camera, CameraAdmin)
admin.site.register(Face, FaceAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Zone, ZoneAdmin)
