from index.base.repository import Base


class FeatureRepository(Base):

    @classmethod
    def model(cls):
        from .model import Feature

        return Feature

    @classmethod
    def admin_view(cls):
        from .admin import Feature

        return Feature

    @classmethod
    def actions(cls):
        from .validator import Create, Update

        return {
            'create': Create,
            'update': Update
        }

    @classmethod
    def serializers(cls):
        from .serializer import BaseFeature

        return {
            'base': BaseFeature,
        }
