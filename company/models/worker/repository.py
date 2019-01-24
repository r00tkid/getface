from index.base.repository import Base


class WorkerRepository(Base):

    @classmethod
    def model(cls):
        from .model import Worker

        return Worker

    @classmethod
    def admin_view(cls):
        from .admin import Worker

        return Worker

    @classmethod
    def actions(cls):
        from .validator import Register, Create, Update

        return {
            'register': Register,
            'create': Create,
            'update': Update,
        }

    @classmethod
    def serializers(cls):
        from .serializer import BaseWorker, ExtendedWorker

        return {
            'base': BaseWorker,
            'extended': ExtendedWorker,
        }
