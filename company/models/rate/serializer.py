from index.base.repository import Base


class RateSerializer(Base.Serializer):
    class Meta:
        from .model import Rate

        model = Rate
        fields = ('id', 'name', 'description', 'per_month', 'lifetime',)
