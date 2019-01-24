from index.base.repository import Base


class UserRepository(Base):

    @classmethod
    def model(cls):
        from .model import User

        return User

    @classmethod
    def admin_view(cls):
        from .admin import User

        return User

    @classmethod
    def actions(cls):
        from .validator import Register, Update

        return {
            'register': Register,
            'update': Update
        }

    @classmethod
    def serializers(cls):
        from .serializer import BaseUser, ExtendedUser

        return {
            'base': BaseUser,
            'extended': ExtendedUser,
        }
