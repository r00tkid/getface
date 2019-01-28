import typing as tp
from index.base.repository import Base


class ProgressRepository(Base):
    from .model import Progress as __Model
    from .admin import Progress as __Admin
    from .validator import Create as __Create
    from .serializer import BaseProgress as __BaseProgress

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
    def serializers(cls) -> tp.Dict[str, tp.Union[tp.Type[__BaseProgress]]]:
        return {
            'base': cls.__BaseProgress,
        }
