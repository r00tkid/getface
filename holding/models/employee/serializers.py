from rest_framework.serializers import SerializerMethodField as _Method
from rest_framework.serializers import ModelSerializer as _Serializer
from app.base.exceptions import APIException as _Exception
from rest_framework import serializers as _se
from rest_framework import status as _status
from django.db import transaction as _ts


class EmployeeCreateSerializer(_Serializer):
    first_name = _se.CharField(
        required=True,
        min_length=2,
        max_length=200,
    )

    last_name = _se.CharField(
        required=True,
        min_length=2,
        max_length=200,
    )

    phone = _se.IntegerField(
        required=True,
        allow_null=True,
    )

    company_id = _se.IntegerField(
        required=True,
    )

    is_manager = _se.BooleanField(
        required=False,
        default=False,
    )

    is_fired = _se.BooleanField(
        required=False,
        default=False,
    )

    email = _se.EmailField(
        required=False,
        min_length=6,
        max_length=255,
    )

    time_zone = _se.CharField(
        required=False,
        default="UTC",
        min_length=3,
    )

    position_id = _se.IntegerField(
        required=True,
    )

    @_ts.atomic
    def create(self, validated_data):
        """
        :type validated_data: dict
        """
        from holding.models import Employee, Position
        from django.db.models import Q
        from entry.models import User

        email = validated_data.get('email')
        phone = validated_data.get('phone')
        position = Position.get_by_id(validated_data.get('position_id'))

        if not email and not phone:
            return Employee(**validated_data)

        user = User.objects.filter(Q(email=email) | Q(phone=phone)).first()

        validated_data['timezone'] = validated_data.pop('time_zone')
        employee = Employee(**validated_data)
        employee.new_invitation()

        if user:
            check = Employee.objects.filter(user=user, company_id=validated_data.get('company_id'))

            if check:
                raise _Exception({
                    'detail': 'You can\'t assign same worker to company twice',
                }, status_code=_status.HTTP_409_CONFLICT)

            employee.user = user
            employee.is_active = user.is_active
            employee.is_invited = True
            employee.auth_key = None
        else:
            employee.create_user()

        employee.set_position(position)
        employee.save()

        return employee

    def get_time_zone(self, employee):
        if isinstance(employee.timezone, str):
            return employee.timezone
        else:
            return employee.timezone.zone

    class Meta:
        from .model import Employee as _Employee

        model = _Employee
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'company_id', 'is_manager', 'is_fired', 'time_zone', 'position_id')


class EmployeeUpdateSerializer(_Serializer):
    first_name = _se.CharField(
        required=False,
        min_length=2,
        max_length=200,
    )

    last_name = _se.CharField(
        required=False,
        min_length=2,
        max_length=200,
    )

    phone = _se.IntegerField(
        required=False,
        allow_null=True,
    )

    is_manager = _se.BooleanField(
        required=False,
        default=False,
    )

    is_fired = _se.BooleanField(
        required=False,
        default=False,
    )

    email = _se.EmailField(
        required=False,
        min_length=6,
        max_length=255,
    )

    time_zone = _se.CharField(
        required=False,
        default="UTC",
        min_length=3,
    )

    position_id = _se.IntegerField(
        required=False,
    )

    @_ts.atomic
    def update(self, employee, validated_data):
        """
        :type employee: holding.models.Employee
        :type validated_data: dict
        """
        employee.update(validated_data)

        return employee

    def get_time_zone(self, employee):
        if isinstance(employee.timezone, str):
            return employee.timezone
        else:
            return employee.timezone.zone

    class Meta:
        from .model import Employee as _Employee

        model = _Employee
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'company_id', 'is_manager', 'is_fired', 'time_zone', 'position_id')


class EmployeeSerializer(_Serializer):
    time_zone = _Method()

    def get_time_zone(self, model):
        return model.timezone.zone

    class Meta:
        from .model import Employee as _Employee

        model = _Employee
        fields = ('id', 'first_name', 'last_name', 'email', 'time_zone',)


class EmployeeExtendedSerializer(_Serializer):
    email = _Method('get_worker_email')
    physical = _Method('get_worker_has_physical_user')
    time_zone = _Method()

    def get_time_zone(self, employee):
        if isinstance(employee.timezone, str):
            return employee.timezone
        else:
            return employee.timezone.zone

    def get_worker_email(self, model):
        if model.email and model.email != "":
            return model.email

        if model.user_id:
            return model.user.email

        return None

    def get_worker_has_physical_user(self, model):
        return bool(model.user_id)

    class Meta:
        from .model import Employee as _Employee

        model = _Employee
        fields = ('id', 'first_name', 'last_name', 'is_fired', 'is_manager', 'email', 'physical', 'time_zone',)
