from rest_framework.serializers import SerializerMethodField as _Method
from rest_framework.serializers import ModelSerializer as _Serializer
from rest_framework import serializers as _se
from django.db import transaction as _ts


class PositionSerializer(_Serializer):
    departments = _Method()

    def get_departments(self, position):
        return position.departments.values_list('department_id', flat=True)

    class Meta:
        from .model import Position as _Position

        model = _Position
        fields = ('name', 'company_id', 'id', 'departments',)


class PositionCreateSerializer(_Serializer):
    name = _se.CharField(
        required=True,
        min_length=2,
        max_length=255,
    )

    department_id = _se.IntegerField(
        required=True,
    )

    @_ts.atomic
    def create(self, validated_data):
        """
        :type validated_data: dict
        """
        from holding.models import Department

        department = Department.get_by_id(validated_data.pop('department_id'))
        position = department.create_position(**validated_data)

        return position

    class Meta:
        from .model import Position as _Position

        model = _Position
        fields = ('name', 'company_id', 'department_id', 'id')


class PositionUpdateSerializer(_Serializer):
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
        from .model import Position as _Position

        model = _Position
        fields = ('name', 'company_id', 'id',)
