import typing as tp
from index.base.repository import Base


class UserRepository(Base):
    from .model import User as __Model
    from .admin import User as __Admin
    from .validator import Register as __Register, Update as __Update
    from .serializer import BaseUser as __BaseUser, ExtendedUser as __ExtendedUser

    @classmethod
    def model(cls) -> tp.Type[__Model]:
        return cls.__Model

    @classmethod
    def admin_view(cls) -> tp.Type[__Admin]:
        return cls.__Admin

    @classmethod
    def actions(cls) -> tp.Dict[str, tp.Union[tp.Type[__Register], tp.Type[__Update]]]:
        return {
            'register': cls.__Register,
            'update': cls.__Update,
        }

    @classmethod
    def serializers(cls) -> tp.Dict[str, tp.Union[tp.Type[__BaseUser], tp.Type[__ExtendedUser]]]:
        return {
            'base': cls.__BaseUser,
            'extended': cls.__ExtendedUser,
        }
