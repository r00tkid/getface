from rest_framework.serializers import SerializerMethodField as _Method
from rest_framework.serializers import ModelSerializer as _Serializer


class LogbookSerializer(_Serializer):
    time_zone = _Method()

    def get_time_zone(self, model):
        return model.timezone.zone

    class Meta:
        from .model import Logbook as _Logbook

        model = _Logbook
        fields = ('id', 'employee_id', 'start', 'end', 'activity', 'mood', 'fatigue', 'time_zone',)
