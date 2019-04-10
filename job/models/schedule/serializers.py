from rest_framework.serializers import ModelSerializer as _Serializer
from rest_framework.serializers import SerializerMethodField as _Method


class ScheduleSerializer(_Serializer):
    time_zone = _Method()

    def get_time_zone(self, model):
        return model.timezone.zone

    class Meta:
        from .model import Schedule as _Schedule

        model = _Schedule
        fields = ('id', 'employee_id', 'start', 'end', 'is_wanted', 'time_zone',)
