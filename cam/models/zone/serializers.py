from rest_framework.serializers import ModelSerializer as _Serializer


class ZoneSerializer(_Serializer):
    class Meta:
        from .model import Zone as _Zone

        model = _Zone
        fields = ('id', 'name', 'company_id',)
