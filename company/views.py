from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from company.serializers import CompanySerializer, WorkerSerializer
from company.models import Company, Worker


@api_view(['GET'])
def get_companies(request):
    return Response(
        {
            'name': 'Companies view',
            'companies': CompanySerializer(
                Company.objects.all(),
                many=True,
            ).data,
        }, status=status.HTTP_200_OK
    )


@api_view(['GET'])
@permission_classes([AllowAny])
def get_company_workers(request, company_id):
    if False:
        # todo: move False after tests
        user = request.user

        try:
            company = Company.objects.get(id=company_id)
            manager = Worker.objects.filter(company_id=company_id, user_id=user.id).first()

            if user.id != company.owner_id and not manager.is_manager:
                return Response({
                    'message': 'You have no power here.'
                }, status=status.HTTP_403_FORBIDDEN)
        except:
            return Response({
                'message': 'No such company or you not work for it or you don\'t have right permissions.'
            }, status=status.HTTP_404_NOT_FOUND)

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
            'name': 'Workers view',
            'workers': WorkerSerializer(
                objects,
                many=True,
            ).data,
        }, status=status.HTTP_200_OK
    )


@api_view(['GET'])
@permission_classes([AllowAny])
def get_company_view(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except:
        company = {}

    return Response(
        {
            'name': 'Company [%s] view' % (company.name if bool(company) else company_id),
            'company': CompanySerializer(company).data if bool(company) else {},
        }, status=status.HTTP_200_OK if bool(company) else status.HTTP_404_NOT_FOUND
    )
