from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from company.base.permissions import CanManageCompany
from company.serializers import WorkerSerializer
from company.models import Worker, Company
from company.base.exceptions import NotFound


@api_view(('GET',))
@permission_classes((CanManageCompany,))
def get_company_workers(request, company_id):
    query = request.GET
    objects = Worker.objects.filter(company_id=company_id)

    is_fired = query.get('fired')
    is_manager = query.get('manager')
    is_worker = query.get('worker')

    if is_fired != '':
        objects = objects.filter(is_fired=False)

    if is_manager == '':
        objects = objects.filter(is_manager=True)

    if is_worker == '':
        objects = objects.filter(is_manager=False)

    return Response(
        {
            'detail': 'Workers view',
            'workers': WorkerSerializer(
                objects,
                many=True,
            ).data,
        }, status=status.HTTP_200_OK
    )


@api_view(('GET',))
# Default auth permission
def get_user_status(request, company_id):
    try:
        company = Company.objects.get(pk=company_id)
    except:
        raise NotFound

    user = request.user

    worker = Worker.objects.filter(user=user, company=company).first()
    deleted = Worker.all_objects.filter(user=user, company=company).first()

    return Response({
        'is_owner': company.owner_id == user.id,
        'is_worker': bool(worker),
        'is_manager': worker.is_manager if bool(worker) else False,
        'is_fired': worker.is_fired if bool(worker) else True if company.owner_id != user.id else False,
        'is_deleted': bool(deleted.deleted_at) if deleted else False,
    })


@api_view(('GET',))
# Default auth permission
def get_user_worker(request, company_id):
    try:
        company = Company.objects.get(pk=company_id)
    except:
        raise NotFound

    user = request.user
    worker = Worker.objects.filter(user=user, company=company).first()

    return Response({
        'detail': 'Your company profile' if worker else 'You are not the part of this company or not in workers',
        'worker': WorkerSerializer(instance=worker).data if worker else None,
    }, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION if worker else status.HTTP_403_FORBIDDEN)
