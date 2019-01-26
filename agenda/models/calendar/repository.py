from index.base.repository import Base
from index.base.exceptions import ToDo


class CalendarRepository(Base):
    @classmethod
    def model(cls):
        from .model import Calendar

        return Calendar

    @classmethod
    def admin_view(cls):
        from .admin import Calendar

        return Calendar

    @classmethod
    def actions(cls):
        from .validator import Create

        return {
            'create': Create,
        }

    @classmethod
    def serializers(cls):
        from .serializer import BaseCalendar

        return {
            'base': BaseCalendar
        }
