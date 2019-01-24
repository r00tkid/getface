from index.base.repository import Base


class RateRepository(Base):

    @classmethod
    def model(cls):
        from .model import Rate

        return Rate

    @classmethod
    def admin_view(cls):
        from .admin import Rate

        return Rate

    @classmethod
    def actions(cls):
        from .validator import Create, Update

        return {
            'create': Create,
            'update': Update
        }

    @classmethod
    def serializers(cls):
        from .serializer import BaseRate

        return {
            'base': BaseRate,
        }
