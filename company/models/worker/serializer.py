from index.base.repository import Base
from .model import Worker


class BaseWorker(Base.Serializer):
    class Meta:
        model = Worker
        fields = ('id', 'first_name', 'last_name', 'email',)


class ExtendedWorker(Base.Serializer):
    serial = Base.Serializer.serializers

    email = serial.SerializerMethodField('get_worker_email')
    physical = serial.SerializerMethodField('get_worker_has_physical_user')

    def get_worker_email(self, model):
        if model.email and model.email != "":
            return model.email

        if model.user_id:
            return model.user.email

        return None

    def get_worker_has_physical_user(self, model):
        return bool(model.user_id)

    class Meta:
        model = Worker
        fields = ('id', 'first_name', 'last_name', 'is_fired', 'is_manager', 'email', 'physical',)
