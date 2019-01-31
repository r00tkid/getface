import typing as tp
from index.base.repository import Base


class DiscountRepository(Base):
    from .model import Discount as __Model
    from .admin import Discount as __Admin
    from .validator import Create as __Create
    from .serializer import BaseDiscount as __BaseDiscount

    @classmethod
    def model(cls) -> tp.Type[__Model]:
        return cls.__Model

    @classmethod
    def admin_view(cls) -> tp.Type[__Admin]:
        return cls.__Admin

    @classmethod
    def actions(cls) -> tp.Dict[str, tp.Union[tp.Type[__Create]]]:
        return {
            'create': cls.__Create,
        }

    @classmethod
    def serializers(cls) -> tp.Dict[str, tp.Union[tp.Type[__BaseDiscount]]]:
        return {
            'base': cls.__BaseDiscount,
        }
