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
            'valid': False,
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
        'valid': True,
        'token': token,  # todo: send mail instead
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def worker_sign_up(request):
    from form.modules.autentication import WorkerRegistration
    validator = WorkerRegistration(data=request.data)

    if not validator.validate():
        Response({
            'valid': False,
            'errors': validator.errors,
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    data = validator.data

    try:
        worker = Worker.objects.get(auth_key=data.get('uuid'))
        user = User.objects.get(id=worker.user_id)
    except:
        return Response({
            'valid': False,
            'message': 'Did you have been invited successfully?',
        }, status=status.HTTP_404_NOT_FOUND)

    if request.user:
        if worker.user_id != request.user.id:
            return Response({
                'valid': False,
                'message': "Get log out to perform this action."
            }, status=status.HTTP_403_FORBIDDEN)

        worker.auth_key = None
        worker.save()

        return Response({
            'valid': True,
            'message': "You already in system."
        })

    if not user.is_active and not user.is_superuser:
        user.username = data.get('username')
        user.set_password(data.get('password'))
        user.is_active = True
        user.save()

    worker.auth_key = None
    worker.save()

    return Response({
        'valid': True,
        'token': create_token(user),
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def reset_password(request):
    pass  # todo: do


@api_view(['POST'])
@permission_classes([AllowAny])
def reset_confirm(request):
    pass  # todo: do
