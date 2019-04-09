from rest_framework.serializers import ModelSerializer as _Serializer
from .model import Feature as _Feature


class FeatureSerializer(_Serializer):
    class Meta:
        model = _Feature
        fields = ('id', 'name', 'description', 'link', 'is_alive', 'is_important')
