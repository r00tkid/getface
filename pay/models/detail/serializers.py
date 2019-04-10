from rest_framework.serializers import ModelSerializer as _Serializer


class PaymentDetailsSerializer(_Serializer):
    class Meta:
        from .model import PaymentDetails as _Details

        model = _Details
        fields = ('id', 'company_id', 'rate_id', 'discount_id', 'start', 'discount_percent',)
