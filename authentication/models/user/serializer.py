from index.base.repository import Base
from authentication.models.user.model import get_user_model


class UserSerializer(Base.Serializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'first_name', 'last_name', 'email', 'is_active', 'is_superuser', 'is_staff')
