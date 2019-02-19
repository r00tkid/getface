from index.base.repository import Base
from .model import Position


class BasePosition(Base.Serializer):
    class Meta:
        model = Position
        fields = ('name', 'company', 'id')
