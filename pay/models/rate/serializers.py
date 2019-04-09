from rest_framework.serializers import SerializerMethodField as _Method
from rest_framework.serializers import ModelSerializer as _Serializer


class RateSerializer(Base.Serializer):
    class Meta:
        from .model import Rate

        model = Rate
        fields = ('id', 'name', 'description', 'per_month', 'lifetime',)
