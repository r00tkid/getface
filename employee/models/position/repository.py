import typing as tp
from index.base.repository import Base


class PositionRepository(Base):
    from .model import Position as __Model
    from .validator import Create as __Create, Update as __Update
    from .serializer import BasePosition as __BasePosition

    @classmethod
    def model(cls) -> tp.Type[__Model]:
        return cls.__Model

    @classmethod
    def admin_view(cls):
        raise NotImplemented

    @classmethod
    def actions(cls) -> tp.Dict[str, tp.Union[tp.Type[__Create], tp.Type[__Update]]]:
        return {
            'create': cls.__Create,
            'update': cls.__Update,
        }

    @classmethod
    def serializers(cls) -> tp.Dict[str, tp.Union[tp.Type[__BasePosition]]]:
        return {
            'base': cls.__BasePosition,
        }
