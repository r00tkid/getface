from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Company

        model = Company
        fields = ('name')


class WorkerSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
        source='user_id.email'
    )

    class Meta:
        from .models import Worker

        model = Worker
        fields = ('first_name', 'last_name', 'email')
