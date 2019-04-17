from rest_framework.serializers import SerializerMethodField as _Method
from rest_framework.serializers import ModelSerializer as _Serializer
from .model import User as _User


class UserRegisterSerializer(_Serializer):
    from rest_framework import serializers as _se
    from rest_framework import validators as _val

    email = _se.EmailField(
        required=True,
        allow_null=False,
        allow_blank=False,
        min_length=6,
        max_length=256,
        validators=[
            _val.UniqueValidator(queryset=_User.objects.all())
        ]
    )

    phone = _se.IntegerField(
        required=True,
        allow_null=False,
        validators=[
            _val.UniqueValidator(queryset=_User.objects.all())
        ]
    )

    password = _se.CharField(
        min_length=6,
        write_only=True,
    )

    first_name = _se.CharField(
        min_length=2,
        max_length=256,
    )

    last_name = _se.CharField(
        min_length=2,
        max_length=256,
    )

    username = _se.CharField(
        min_length=4,
        max_length=256,
    )

    from django.db import transaction as _trans

    @_trans.atomic()
    def create(self, validated_data):
        from django.conf import settings

        user = _User.objects.create(**validated_data)
        user.set_password(validated_data['password'])

        if settings.DEBUG:
            user.activate()
        else:
            user.save()

        if not settings.DEBUG:
            user.mail_activation()

        return user

    class Meta:
        model = _User
        fields = ('email', 'phone', 'password', 'first_name', 'last_name', 'username')


class UserSerializer(_Serializer):
    time_zone = _Method()

    def get_time_zone(self, model):
        return model.timezone.zone

    class Meta:
        model = _User
        fields = ('id', 'first_name', 'last_name', 'username', 'time_zone')


class UserExtendedSerializer(_Serializer):
    last_login = _Method()
    time_zone = _Method()

    def get_time_zone(self, model):
        return model.timezone.zone

    def get_last_login(self, model):
        """@type model: BaseUser"""
        return model.last_login if not model.is_superuser else None

    class Meta:
        model = _User

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
            'time_zone',
        )
