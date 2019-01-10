from rest_framework import serializers
from logging import getLogger
from company.models import Worker
from authentication.serializers import UserSerializer

log = getLogger('django')


class WorkerSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField('get_worker_email')
    physical = serializers.SerializerMethodField('get_worker_has_physical_user')

    def get_worker_email(self, model):
        if model.user_id:
            return model.user.email
        return None

    def get_worker_has_physical_user(self, model):
        return bool(model.user_id)

    class Meta:
        model = Worker
        fields = ('id', 'first_name', 'last_name', 'email', 'physical')


class CompanySerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    @staticmethod
    def get_workers(model):
        return WorkerSerializer(Worker.objects.filter(company=model), many=True).data

    @staticmethod
    def get_owner(model):
        return UserSerializer(model.owner).data

    class Meta:
        from .models import Company

        model = Company
        fields = ('id', 'name', 'description', 'address', 'email', 'phone', 'owner')
