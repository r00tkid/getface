from rest_framework.serializers import SerializerMethodField as _Method
from rest_framework.serializers import ModelSerializer as _Serializer
from .model import User as _User


class UserSerializer(_Serializer):
    time_zone = _Method()

    def get_time_zone(self, model):
        return model.timezone.zone

    class Meta:
        model = _User
        fields = ('id', 'first_name', 'last_name', 'username', 'time_zone')


class UserExtendedSerializer(_Serializer):
    last_login = _Method()
    time_zone = _Method()

    def get_time_zone(self, model):
        return model.timezone.zone

    def get_last_login(self, model):
        """@type model: BaseUser"""
        return model.last_login if not model.is_superuser else None

    class Meta:
        model = _User

        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'is_active',
            'is_staff',
            'is_superuser',
            'date_joined',
            'last_login',
            'time_zone',
        )
