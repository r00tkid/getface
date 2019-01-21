__all__ = ('UserSerializer',)

from rest_framework.serializers import ModelSerializer
from authentication.models.user.model import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'is_active', 'is_superuser', 'is_staff')
