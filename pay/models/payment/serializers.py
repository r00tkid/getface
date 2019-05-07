from rest_framework.serializers import ModelSerializer as _Serializer


class PaymentSerializer(_Serializer):
    class Meta:
        from .model import Payment as _Pay

        model = _Pay
        fields = ('id', 'user_id', 'discount_id', 'details_id', 'info',)
