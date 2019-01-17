from rest_framework.serializers import ModelSerializer
from agenda.models import WorkerAgenda, WorkerFaceTime


class AgendaSerializer(ModelSerializer):
    class Meta:
        model = WorkerAgenda
        fields = ('id', 'start', 'end', 'is_wanted', 'worker_id')


class FaceTimeSerializer(ModelSerializer):
    class Meta:
        model = WorkerFaceTime
        fields = ('id', 'start', 'end', 'active', 'mood', 'worker_id')
