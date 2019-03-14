import os

from django.db.models.query import Q

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from authentication.models import User, get_user_by_id as _get_user
from company.models import Company
from employee.models import Employee
from index.base.exceptions import UnprocessableEntity, APIException

from index.mail.sender import Sandman
from index import settings


def _user_response(user, with_token=False, with_companies=False, detail="OK"):
    if not user:
        raise APIException({
            'detail': 'No user. Incorrect usage.'
        }, status_code=417)

    token = None
    companies = None

    if with_token:
        token = user.get_token()

    if with_companies:
        companies = Company.model.objects.filter(Q(owner=user) | Q(employee__user=user).add(Q(employee__is_fired=False), Q.AND).add(Q(employee__is_active=True), Q.AND))
        serializer = Company.serializers.extended(instance=companies, many=True).add_rights(user, True)
        companies = serializer.data

    serializer = User.serializers.extended if with_companies else User.serializers.base

    return Response({
        'detail': detail,
        'token': token,
        'user': serializer(instance=user).data,
        'companies': companies,
    })


@api_view(['GET', 'HEAD'])
def self_info(request):
    return _user_response(request.user, with_companies=True)


@api_view(['POST'])
@permission_classes((AllowAny,))
def sign_up(request):
    validator = User.validators.create(data=request.data)

    if not validator.validate():
        raise UnprocessableEntity({
            'detail': 'Data has invalid fields.',
            'valid': False,
            'errors': validator.errors,
        }, status.HTTP_422_UNPROCESSABLE_ENTITY)

    debug = {}
    info = validator.data

    user = User.model(**{
        'username': info.get('username'),
        'email': info.get('email'),
        'first_name': info.get('first_name'),
        'last_name': info.get('last_name'),
        'phone': info.get('phone'),
        'is_active': False,
    })

    user.set_password(info.get('password'))
    user.save()

    Sandman(
        mail_from=settings.EMAIL_ADDRESSES.get('main'),
        mail_to=user.email,
        subject="Registration",
        template='user%sregister' % os.sep,
        context={
            'user': user,
        }
    ).start()

    if settings.DEBUG:
        debug['user'] = {}
        debug['user']['id'] = user.id
        debug['user']['activation'] = user.activation

    return Response({
        'valid': True,
        'detail': 'You have been registered.',
        'debug': debug if settings.DEBUG else None,
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes((AllowAny,))
def employee_sign_up(request):
    validator = Employee.validators.create(data=request.data)

    if not validator.validate():
        return Response({
            'valid': False,
            'errors': validator.errors,
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    data = validator.data

    try:
        employee = Employee.model.objects.get(auth_key=data.get('uuid'))
        user = employee.user
    except Employee.model().DoesNotExist as e:
        return Response({
            'valid': False,
            'message': 'Did you have been invited successfully?',
        }, status=status.HTTP_404_NOT_FOUND)

    if request.user:
        if employee.user_id != request.user.id:
            return Response({
                'valid': False,
                'message': "Get log out to perform this action."
            }, status=status.HTTP_403_FORBIDDEN)

        employee.auth_key = None
        employee.save()

        return Response({
            'valid': True,
            'message': "You already in system."
        })

    if not user.is_active and not user.is_superuser:
        user.username = data.get('username')
        user.set_password(data.get('password'))
        user.is_active = True
        user.save()

    employee.auth_key = None
    employee.save()

    return Response({
        'detail': "OK",
        'token': user.get_token(),
        'companies': _user_response(user, with_companies=True).data.get('companies')
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes((AllowAny,))
def activate_account(request):
    data: dict = request.data
    user = _get_user(int(data.get('user_id')))

    if not user.check_activation(data.get('user_key')) or user.is_active:
        return Response({
            'detail': 'User already has been activated or secret codes not match.',
            'active': user.is_active,
        }, status=status.HTTP_409_CONFLICT)

    user.activation = None
    user.is_active = True
    user.save()

    return _user_response(user, with_token=True, with_companies=True, detail="Account has been activated")


@api_view(['POST'])
@permission_classes((AllowAny,))
def reset_password(request):
    data: dict = request.data
    email = data.get('email')
    debug = {}

    if not email:
        return Response({
            'detail': 'Ups, something goes wrong',
            'email': email,
        }, status=status.HTTP_404_NOT_FOUND)

    user: User.model() = User.model.objects.filter(email=email).first()

    if not user or not user.is_active:
        return Response({
            'detail': 'Are you sure that you activate your account?'
        }, status=status.HTTP_409_CONFLICT)

    user.new_activation()
    user.save()

    if settings.DEBUG:
        debug['user'] = {}
        debug['user']['id'] = user.id
        debug['user']['activation'] = user.activation

    Sandman(
        mail_from=settings.EMAIL_ADDRESSES.get('main'),
        mail_to=user.email,
        subject="Password restoration",
        template='user%snew_password' % os.sep,
        context={
            'user': user,
        }
    ).start()

    return Response({
        'detail': 'Change password action has been activated.'
    })


@api_view(['POST'])
@permission_classes((AllowAny,))
def reset_confirm(request):
    data: dict = request.data
    user = _get_user(int(data.get('user_id')))

    if not user.check_activation(data.get('user_key')) or not user.is_active:
        return Response({
            'detail': 'Already used or user is inactive.',
            'active': user.is_active,
        }, status=status.HTTP_409_CONFLICT)

    password = data.get('password')
    c_password = data.get('password_confirmation')

    if not password or not c_password or password != c_password:
        return Response({
            'detail': 'Password not set or confirmation mismatch'
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    user.set_password(data.get('password'))
    user.save()

    return _user_response(user, True, True, 'New password has been set')


@api_view(['POST'])
@permission_classes((AllowAny,))
def resend_mail_invitation(request):
    if request.data.get('email'):
        email = request.data.get('email')
        user: User.model() = User.model.objects.filter(email=email).first()
    elif request.data.get('user_id'):
        user = _get_user(int(request.data.get('user_id')))
    else:
        return Response({
            'detail': 'Data is wrong.',
        }, status=status.HTTP_406_NOT_ACCEPTABLE)

    if not user or user.is_active:
        return Response({
            'detail': 'User not found or already activated.',
            'active': user.is_active if user else False,
        }, status=status.HTTP_409_CONFLICT)

    user.new_activation()
    user.save()

    Sandman(
        mail_from=settings.EMAIL_ADDRESSES.get('main'),
        mail_to=user.email,
        subject="Repeat registration confirmation",
        template='user%sregister' % os.sep,
        context={
            'user': user,
        }
    ).start()

    return Response({
        'detail': 'All is ok'
    })
