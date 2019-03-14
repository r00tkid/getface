from index.base.repository import Base
from .model import User
from rest_framework import serializers


class UserSerializer(Base.Serializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'timezone')


class UserExtendedSerializer(Base.Serializer):
    last_login = serializers.SerializerMethodField()

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
            'timezone',
        )
