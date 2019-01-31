import typing as tp
from index.base.repository import Base


class WorkerRepository(Base):
    from .model import Worker as __Model
    from .admin import Worker as __Admin
    from .validator import Register as __Register, Create as __Create, Update as __Update
    from .serializer import BaseWorker as __BaseWorker, ExtendedWorker as __ExtendedWorker

    @classmethod
    def model(cls) -> tp.Type[__Model]:
        return cls.__Model

    @classmethod
    def admin_view(cls) -> tp.Type[__Admin]:
        return cls.__Admin

    @classmethod
    def actions(cls) -> tp.Dict[str, tp.Union[tp.Type[__Register], tp.Type[__Create], tp.Type[__Update]]]:
        return {
            'register': cls.__Register,
            'create': cls.__Create,
            'update': cls.__Update,
        }

    @classmethod
    def serializers(cls) -> tp.Dict[str, tp.Union[tp.Type[__BaseWorker], tp.Type[__ExtendedWorker]]]:
        return {
            'base': cls.__BaseWorker,
            'extended': cls.__ExtendedWorker,
        }
