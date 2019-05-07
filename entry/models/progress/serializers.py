from rest_framework.serializers import ModelSerializer as _Serializer


class ProgressSerializer(_Serializer):
    class Meta:
        from .model import Progress as _Progress

        model = _Progress
        fields = ('user', 'feature')
