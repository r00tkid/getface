from index.base.repository import Base
from .model import Discount


class DiscountSerializer(Base.Serializer):
    class Meta:
        model = Discount
        fields = ('id', 'name', 'percent',)
