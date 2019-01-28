import typing as tp
from index.base.repository import Base


class RateRepository(Base):
    from .model import Rate as __Model
    from .admin import Rate as __Admin
    from .validator import Create as __Create, Update as __Update
    from .serializer import BaseRate as __BaseRate

    @classmethod
    def model(cls) -> tp.Type[__Model]:
        return cls.__Model

    @classmethod
    def admin_view(cls) -> tp.Type[__Admin]:
        return cls.__Admin

    @classmethod
    def actions(cls) -> tp.Dict[str, tp.Union[tp.Type[__Create], tp.Type[__Update]]]:
        return {
            'create': cls.__Create,
            'update': cls.__Update,
        }

    @classmethod
    def serializers(cls) -> tp.Dict[str, tp.Union[tp.Type[__BaseRate]]]:
        return {
            'base': cls.__BaseRate,
        }
