from rest_framework.serializers import SerializerMethodField as _Method
from rest_framework.serializers import ModelSerializer as _Serializer

from .model import Position


class PositionSerializer(Base.Serializer):
    class Meta:
        model = Position
        fields = ('name', 'company', 'id')
