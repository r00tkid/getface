from index.base.repository import Base
from .model import Discount


class BaseDiscount(Base.Serializer):
    class Meta:
        model = Discount
        fields = ('id', 'name', 'percent',)
