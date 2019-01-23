from index.base.repository import Base
from index.base.exceptions import NotFound
from index import settings


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
    def action(cls, name):
        return cls.actions()[name]

    @classmethod
    def serializers(cls):
        from .serializer import BaseUser, ExtendedUser

        return {
            'base': BaseUser,
            'extended': ExtendedUser,
        }

    @classmethod
    def serializer(cls, name):
        return cls.serializers()[name]

    @classmethod
    def new(cls, data):
        """
        Don't use this method directly, until some special reasons.

        @param data: Data for user creation.
        @type data: dict
        """
        return cls.model()(**data)

    @classmethod
    def info(cls, pk, name=None, api_exception=True):
        obj = cls.model().objects

        try:
            user = obj.get(pk=pk)
        except Exception as e:
            if api_exception:
                raise NotFound({
                    'detail': '%(model)s id:[%(id)d] has not been found.' % {
                        'model': type(cls.model()).__name__,
                        'id': pk
                    },
                    'debug': str(e) if settings.DEBUG else None,
                })
            else:
                return None

        return cls.serializer(name=name if name else 'base')(instance=user)
