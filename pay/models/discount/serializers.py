from rest_framework.serializers import SerializerMethodField as _Method
from rest_framework.serializers import ModelSerializer as _Serializer

from .model import Discount


class DiscountSerializer(Base.Serializer):
    class Meta:
        model = Discount
        fields = ('id', 'name', 'percent',)
