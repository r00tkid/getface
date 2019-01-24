from index.base.repository import Base
from index.base.exceptions import ToDo


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
        raise ToDo

    @classmethod
    def serializers(cls):
        from .serializer import BaseAgenda

        return {
            'base': BaseAgenda,
        }
