from index.base.repository import Base
from .model import Employee


class EmployeeSerializer(Base.Serializer):
    serializers = Base.serializers

    time_zone = serializers.SerializerMethodField()

    def get_time_zone(self, model):
        return model.timezone.zone

    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'email', 'time_zone',)


class EmployeeExtendedSerializer(Base.Serializer):
    serializers = Base.serializers

    email = serializers.SerializerMethodField('get_worker_email')
    physical = serializers.SerializerMethodField('get_worker_has_physical_user')
    time_zone = serializers.SerializerMethodField()

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
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'is_fired', 'is_manager', 'email', 'physical', 'time_zone',)
