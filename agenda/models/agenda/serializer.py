from index.base.repository import Base
from .model import Agenda


class AgendaSerializer(Base.Serializer):
    class Meta:
        model = Agenda
        fields = ('id', 'start', 'end', 'worker_id', 'active', 'mood', 'fatigue')
