from index.base.repository import Base
from .model import Calendar


class CalendarSerializer(Base.Serializer):
    class Meta:
        model = Calendar
        fields = ('id', 'start', 'end', 'is_wanted', 'worker_id')
