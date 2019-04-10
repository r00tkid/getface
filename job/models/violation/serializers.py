from rest_framework.serializers import SerializerMethodField as _Method
from rest_framework.serializers import ModelSerializer as _Serializer


class ViolationSerializer(_Serializer):
    time_zone = _Method()

    def get_time_zone(self, model):
        return model.timezone.zone

    class Meta:
        from .model import Violation as _Violation

        model = _Violation
        fields = ('id', 'employee_id', 'when', 'title', 'description', 'time_zone',)
