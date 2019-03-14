from index.base.repository import Base
from .model import User


class UserSerializer(Base.Serializer):
    serializers = Base.serializers

    time_zone = serializers.SerializerMethodField()

    def get_time_zone(self, model):
        return model.timezone.zone

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'time_zone')


class UserExtendedSerializer(Base.Serializer):
    serializers = Base.serializers

    last_login = serializers.SerializerMethodField()
    time_zone = serializers.SerializerMethodField()

    def get_time_zone(self, model):
        return model.timezone.zone

    def get_last_login(self, model):
        """@type model: BaseUser"""
        return model.last_login if not model.is_superuser else None

    class Meta:
        model = User

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
