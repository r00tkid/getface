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
def get_workers(request):
    return Response(
        {
            'name': 'Workers view',
            'workers': WorkerSerializer(
                Worker.objects.all(),
                many=True,
            ).data,
        }, status=status.HTTP_200_OK
    )


@api_view(['GET'])
@permission_classes([AllowAny])
def get_company_workers(request, company_id):
    return Response(
        {
            'name': 'Workers view',
            'workers': WorkerSerializer(
                Worker.objects.filter(company_id=company_id),
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
