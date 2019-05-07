from rest_framework.serializers import ModelSerializer as _Serializer


class CameraSerializer(_Serializer):
    class Meta:
        from .model import Camera as _

        model = _
        fields = ('id', "name", "ip_address", "is_active", "company_id", "zone_id",)
