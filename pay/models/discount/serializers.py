from rest_framework.serializers import ModelSerializer as _Serializer


class DiscountSerializer(_Serializer):
    class Meta:
        from .model import Discount as _Discount

        model = _Discount
        fields = ('id', 'name', 'percent',)
