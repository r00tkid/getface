from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import User, UserSerializer
from company.models import Company
from .validators import password_validation
from .jwt import create_token


@api_view(
    ['GET', 'HEAD', 'POST', 'OPTIONS', 'PATCH', 'PUT',
     'DELETE', 'COPY', 'LINK', 'UNLINK', 'PURGE', 'LOCK',
     'UNLOCK', 'PROPFIND', 'VIEW'])
def self_info(request):
    return Response(UserSerializer(User.objects.get(id=request.user.id)).data)


@api_view(['POST'])
@permission_classes([AllowAny])
def sign_up(request):
    owner_info = {
        'username': request.data.get('username').strip(),
        'email': request.data.get('email').strip(),
        'first_name': request.data.get('first_name').strip(),
        'last_name': request.data.get('last_name').strip(),
        'is_active': False,
    }

    (user, error) = password_validation(
        str(request.data.get('password')),
        str(request.data.get('password_confirmation')),
        owner_info
    )

    if None != error:
        return Response({
            'message': 'Password has errors',
            'errors': error
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    user.save()
    user = User.objects.get(username=user.username)

    company_info = {
        'name': request.data.get('company'),
        'address': request.data.get('address'),
        'phone': request.data.get('phone'),
        'email': request.data.get('company_email', user.email),
        'owner_id': user.id,
    }

    company = Company(**company_info)
    company.save()

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
