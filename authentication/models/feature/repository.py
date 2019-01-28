import typing as tp
from index.base.repository import Base


class FeatureRepository(Base):
    from .model import Feature as __Model
    from .admin import Feature as __Admin
    from .validator import Create as __Create, Update as __Update
    from .serializer import BaseFeature as __BaseFeature

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
    def serializers(cls) -> tp.Dict[str, tp.Union[tp.Type[__BaseFeature]]]:
        return {
            'base': cls.__BaseFeature,
        }
