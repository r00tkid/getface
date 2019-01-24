from index.base.repository import Base
from .model import Agenda


class BaseAgenda(Base.Serializer):
    class Meta:
        model = Agenda
        fields = ('id', 'start', 'end', 'is_wanted', 'worker_id')
