from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from authentication.models import User
from company.models import Company, Worker
from authentication.jwt import create_token
from index.base.exceptions import UnprocessableEntity


@api_view(
    ['GET', 'HEAD', 'POST', 'OPTIONS', 'PATCH', 'PUT',
     'DELETE', 'COPY', 'LINK', 'UNLINK', 'PURGE', 'LOCK',
     'UNLOCK', 'PROPFIND', 'VIEW'])
def self_info(request):
    companies_owner = Company.serializer('extended')(
        instance=Company.model().objects.filter(owner=request.user),
        many=True
    )

    as_worker = Worker.model().objects.filter(user=request.user).values('company_id')
    compare = Company.model().objects.filter(
        id__in=[c.get('company_id') for c in as_worker]
    ).filter(worker__is_fired=False).distinct()

    companies_worker = Company.serializer('extended')(
        instance=compare.filter(worker__is_manager=False),
        many=True,
    )

    companies_manager = Company.serializer('extended')(
        instance=compare.filter(worker__is_manager=True),
        many=True,
    )

    companies_worker.add_owner()
    companies_worker.add_worker_info(user=request.user, field_name='me')
    companies_manager.add_owner()
    companies_manager.add_worker_info(user=request.user, field_name='me')

    return Response({
        'user': User.serializer('extended')(instance=request.user).data,
        'companies': {
            'owner': companies_owner.data,
            'worker': companies_worker.data,
            'manager': companies_manager.data,
        }
    })


@api_view(['POST'])
@permission_classes((AllowAny,))
def sign_up(request):
    validator = User.action('register')(data=request.data)

    if not validator.validate():
        raise UnprocessableEntity({
            'detail': 'Data has invalid fields.',
            'valid': False,
            'errors': validator.errors,
        })

    info = validator.data

    user = User.new({
        'username': info.get('username'),
        'email': info.get('email'),
        'first_name': info.get('first_name'),
        'last_name': info.get('last_name'),
        'phone': info.get('phone'),
        # todo: change when got smtp server
        'is_active': True,
    })

    user.set_password(info.get('password'))
    user.save()

    token = create_token(user)

    return Response({
        'valid': True,
        'token': token,  # todo: send mail instead
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes((AllowAny,))
def worker_sign_up(request):
    validator = Worker.action('register')(data=request.data)

    if not validator.validate():
        return Response({
            'valid': False,
            'errors': validator.errors,
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    data = validator.data

    try:
        worker = Worker.model().objects.get(auth_key=data.get('uuid'))
        user = worker.user
    except Exception as e:
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
@permission_classes((AllowAny,))
def reset_password(request):
    pass  # todo: do


@api_view(['POST'])
@permission_classes((AllowAny,))
def reset_confirm(request):
    pass  # todo: do
