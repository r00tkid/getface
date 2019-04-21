from rest_framework.serializers import SerializerMethodField as _Method
from rest_framework.serializers import ModelSerializer as _Serializer


class EmployeeCreateSerializer(_Serializer):
    pass


class EmployeeUpdateSerializer(_Serializer):
    pass


class EmployeeSerializer(_Serializer):
    time_zone = _Method()

    def get_time_zone(self, model):
        return model.timezone.zone

    class Meta:
        from .model import Employee as _Employee

        model = _Employee
        fields = ('id', 'first_name', 'last_name', 'email', 'time_zone',)


class EmployeeExtendedSerializer(_Serializer):
    email = _Method('get_worker_email')
    physical = _Method('get_worker_has_physical_user')
    time_zone = _Method()

    def get_time_zone(self, model):
        return model.timezone.zone

    def get_worker_email(self, model):
        if model.email and model.email != "":
            return model.email

        if model.user_id:
            return model.user.email

        return None

    def get_worker_has_physical_user(self, model):
        return bool(model.user_id)

    class Meta:
        from .model import Employee as _Employee

        model = _Employee
        fields = ('id', 'first_name', 'last_name', 'is_fired', 'is_manager', 'email', 'physical', 'time_zone',)
