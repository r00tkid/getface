from rest_framework.serializers import ModelSerializer as _Serializer


class RateSerializer(_Serializer):
    class Meta:
        from .model import Rate

        model = Rate
        fields = ('id', 'name', 'description', 'per_month', 'lifetime',)
