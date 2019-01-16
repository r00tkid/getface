from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from authentication.serializers import User, UserSerializer
from authentication.jwt import create_token
from company.models import Company, Worker
from company.serializers import CompanyWithWorkersSerializer, CompanyWithOwnerSerializer


@api_view(
    ['GET', 'HEAD', 'POST', 'OPTIONS', 'PATCH', 'PUT',
     'DELETE', 'COPY', 'LINK', 'UNLINK', 'PURGE', 'LOCK',
     'UNLOCK', 'PROPFIND', 'VIEW'])
def self_info(request):
    companies_owner = CompanyWithWorkersSerializer(instance=Company.objects.filter(owner=request.user), many=True)

    as_worker = Worker.objects.filter(user=request.user).values('company_id')
    compare = Company.objects.filter(id__in=[c.get('company_id') for c in as_worker]).filter(worker__is_fired=False)

    companies_worker = CompanyWithOwnerSerializer(instance=compare.filter(worker__is_manager=False), many=True)
    companies_manager = CompanyWithOwnerSerializer(instance=compare.filter(worker__is_manager=True), many=True)

    return Response({
        'user': UserSerializer(request.user).data,
        'companies': {
            'owner': companies_owner.data,
            'worker': companies_worker.data,
            'manager': companies_manager.data,
        }
    })


@api_view(['POST'])
@permission_classes((AllowAny,))
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
        # todo: change when got smtp server
        'is_active': True,
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
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes((AllowAny,))
def worker_sign_up(request):
    from form.modules.autentication import WorkerRegistration
    validator = WorkerRegistration(data=request.data)

    if not validator.validate():
        return Response({
            'valid': False,
            'errors': validator.errors,
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    data = validator.data

    try:
        worker = Worker.objects.get(auth_key=data.get('uuid'))
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
