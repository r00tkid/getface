from rest_framework.serializers import ModelSerializer as _Serializer


class VideoSerializer(_Serializer):
    class Meta:
        from .model import Video as _

        model = _
        fields = ('id', 'start', 'duration', 'filename', 'camera_id')
