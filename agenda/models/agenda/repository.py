from index.base.repository import Base


class AgendaRepository(Base):
    @classmethod
    def model(cls):
        from .model import Agenda

        return Agenda

    @classmethod
    def admin_view(cls):
        from .admin import Agenda

        return Agenda

    @classmethod
    def actions(cls):
        from .validator import Create, Update

        return {
            'create': Create,
            'update': Update,
        }

    @classmethod
    def serializers(cls):
        from .serializer import BaseAgenda

        return {
            'base': BaseAgenda,
        }
