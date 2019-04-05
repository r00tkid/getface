from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from index.base.exceptions import NotFound, APIException
from employee.models import Department
from company.models import Company


@api_view(['GET'])
def get_company_departments(request, company_id):
    company = Company.model.objects.filter(pk=company_id).first()

    if not company:
        raise NotFound()

    raise APIException({
        'detail': 'Not implemented'
    }, status.HTTP_501_NOT_IMPLEMENTED)
