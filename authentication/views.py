from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from authentication.serializers import User, UserSerializer
from authentication.jwt import create_token
from company.models import Company, Worker


@api_view(
    ['GET', 'HEAD', 'POST', 'OPTIONS', 'PATCH', 'PUT',
     'DELETE', 'COPY', 'LINK', 'UNLINK', 'PURGE', 'LOCK',
     'UNLOCK', 'PROPFIND', 'VIEW'])
def self_info(request):
    return Response(UserSerializer(request.user).data)


@api_view(['POST'])
@permission_classes([AllowAny])
def sign_up(request):
    from form.modules.autentication import Registration
    validator = Registration(data=request.data)

    if not validator.validate():
        return Response({
            'message': 'Sorry, your form is invalid.',
            'errors': validator.errors,
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    info = validator.data

    user = User(**{
        'username': info.get('username'),
        'email': info.get('email'),
        'first_name': info.get('first_name'),
        'last_name': info.get('last_name'),
        'is_active': False,
    })

    user.set_password(info.get('password'))
    user.save()

    Company(**{
        'name': info.get('company_name'),
        'address': info.get('company_address'),
        'phone': info.get('company_phone'),
        'email': info.get('company_email'),
        'owner_id': user.id,
    }).save()

    token = create_token(user)

    return Response({
        'message': 'All is ok.',
        'token': token,
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def worker_sign_up(request):
    pass


@api_view(['POST'])
@permission_classes([AllowAny])
def reset_password(request):
    pass


@api_view(['POST'])
@permission_classes([AllowAny])
def reset_confirm(request):
    pass
