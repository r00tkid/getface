from rest_framework.serializers import ModelSerializer as _Serializer
from rest_framework import serializers as _se
from django.db import transaction as _ts


class DepartmentSerializer(_Serializer):
    name = _se.CharField(
        required=True,
        min_length=2,
        max_length=255,
    )

    company_id = _se.IntegerField(
        required=True,
    )

    @_ts.atomic
    def create(self, validated_data):
        """
        :type validated_data: dict
        """
        from holding.models import Department

        department = Department(**validated_data)

        department.save()

        return department

    class Meta:
        from .model import Department as _Department

        model = _Department
        fields = ('name', 'company_id', 'id',)


class DepartmentUpdateSerializer(_Serializer):
    name = _se.CharField(
        required=True,
        min_length=2,
        max_length=255,
    )

    @_ts.atomic
    def update(self, instance, validated_data):
        """
        :type instance: holding.models.Department
        :type validated_data: dict
        """
        instance.update(validated_data, nullable=False)

        return instance

    class Meta:
        from .model import Department as _Department

        model = _Department
        fields = ('name', 'company_id', 'id',)
