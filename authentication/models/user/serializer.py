from index.base.repository import Base
from .model import User
from rest_framework import serializers


class BaseUser(Base.Serializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username')


class ExtendedUser(Base.Serializer):
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
        )
