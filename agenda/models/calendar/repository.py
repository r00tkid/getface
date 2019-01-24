from index.base.repository import Base
from index.base.exceptions import ToDo


class CalendarRepository(Base):
    @classmethod
    def model(cls):
        from .model import Calendar

        return Calendar

    @classmethod
    def admin_view(cls):
        raise ToDo

    @classmethod
    def actions(cls):
        raise ToDo

    @classmethod
    def serializers(cls):
        raise ToDo
