from index.base.repository import Base


class ProgressRepository(Base):

    @classmethod
    def model(cls):
        from .model import Progress

        return Progress

    @classmethod
    def admin_view(cls):
        from .admin import Progress

        return Progress

    @classmethod
    def actions(cls):
        from .validator import Create

        return {
            'create': Create,
        }

    @classmethod
    def serializers(cls):
        from .serializer import BaseProgress

        return {
            'base': BaseProgress,
        }
