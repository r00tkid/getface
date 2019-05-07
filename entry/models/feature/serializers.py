from rest_framework.serializers import ModelSerializer as _Serializer


class FeatureSerializer(_Serializer):
    class Meta:
        from .model import Feature as _Feature

        model = _Feature
        fields = ('id', 'name', 'description', 'link', 'is_alive', 'is_important')
