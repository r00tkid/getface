from index.base.repository import Base
from .model import Feature


class FeatureSerializer(Base.Serializer):
    class Meta:
        model = Feature
        fields = ('id', 'name', 'description', 'link', 'is_alive', 'is_important')
