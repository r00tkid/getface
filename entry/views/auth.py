from entry.models import User, UserExtendedSerializer, UserRegisterSerializer
from holding.models import Employee, Company, CompanyExtendedSerializer
from rest_framework.decorators import api_view, permission_classes
from app.base.exceptions import APIException, UnprocessableEntity
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models.query import Q
from rest_framework import status
from django.conf import settings
from app.mail import Sandman
import os


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
        companies = Company.objects.filter(Q(owner=user) | Q(employee__user=user).add(Q(employee__is_fired=False), Q.AND).add(Q(employee__is_active=True), Q.AND))
        serializer = CompanyExtendedSerializer(instance=companies, many=True).add_rights(user)
        companies = serializer.data

    return Response({
        'detail': detail,
        'token': token,
        'user': UserExtendedSerializer(instance=user).data,
        'companies': companies,
    })


@api_view(['GET', 'HEAD'])
def self_info(request):
    return _user_response(request.user, with_companies=True)


@api_view(['POST'])
@permission_classes((AllowAny,))
def sign_up(request):
    register = UserRegisterSerializer(data=request.data)

    if not register.is_valid():
        raise UnprocessableEntity({
            'detail': 'Data has errors',
            'errors': register.errors,
        })

    user = register.save()

    if settings.DEBUG:
        return Response({
            'detail': 'You have been registered.',
            'valid': True,
            'debug': {
                'user': {
                    'id': user.id,
                    'activation': 'has been activated [debug]',
                }
            },
        }, status=status.HTTP_201_CREATED)

    return Response({
        'detail': 'You have been registered.',
        'valid': True,
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes((AllowAny,))
def employee_sign_up(request):
    # ToDo: this
    # validator = Employee.validators.create(data=request.data)
    #
    # if not validator.validate():
    #     return Response({
    #         'valid': False,
    #         'errors': validator.errors,
    #     }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    data = request.data

    try:
        employee = Employee.objects.get(auth_key=data.get('uuid'))
        user = employee.user
    except Employee.DoesNotExist as e:
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
    data = request.data
    user = User.get_by_id(int(data.get('user_id')))

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

    user = User.objects.filter(email=email).first()

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
    data = request.data
    user = User.get_by_id(int(data.get('user_id')))

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
        user = User.objects.filter(email=email).first()
    elif request.data.get('user_id'):
        user = User.get_by_id(int(request.data.get('user_id')))
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
