import jwt

from django.conf import settings
from app.base.exceptions import APIException

from django.db.models import Q
from django.contrib.auth import authenticate
from django.utils.translation import ugettext as _

from auth.models import User
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.serializers import JSONWebTokenSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


def create_token(user):
    payload = jwt_payload_handler(user)
    token = jwt.encode(payload, settings.SECRET_KEY)
    return token.decode('unicode_escape')


class CustomJWTSerializer(JSONWebTokenSerializer):
    username_field = 'username'

    def validate(self, attrs):
        # credentials (login=email|username|phone)[unique]
        login = attrs.get("username")
        password = attrs.get("password")

        user_obj = User.objects.filter(
            Q(email=login) | Q(username=login) | Q(phone=login)
        ).first()

        if user_obj is not None:
            credentials = {
                'username': user_obj.username,
                'password': password,
            }

            if all(credentials.values()):
                user = authenticate(**credentials)

                if user:
                    if not user.is_active and not user.is_superuser:
                        raise APIException({
                            'detail': _('User account is disabled.'),
                        }, status_code=409)

                    payload = jwt_payload_handler(user)

                    return {
                        'token': jwt_encode_handler(payload),
                        'user': user
                    }
                else:
                    raise APIException({
                        'detail': _('Unable to log in with provided credentials.'),
                    }, status_code=422)

            else:
                raise APIException({
                    'detail': _(
                        'Must include "{username_field}" and "password".'
                    ).format(username_field=self.username_field),
                }, status_code=422)

        else:
            raise APIException({
                'detail': _('Account with this email/username/phone does not exists'),
            }, status_code=404)

    def update(self, instance, validated_data):
        super().update(instance, validated_data)

    def create(self, validated_data):
        super().create(validated_data)
