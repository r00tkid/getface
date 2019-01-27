from index.base.repository import Base


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
        from .validator import Create, Update

        return {
            'create': Create,
            'update': Update,
        }

    @classmethod
    def serializers(cls):
        from .serializer import BaseCalendar

        return {
            'base': BaseCalendar
        }
