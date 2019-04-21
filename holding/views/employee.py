from holding.models import Employee, EmployeeExtendedSerializer, EmployeeCreateSerializer, EmployeeUpdateSerializer
from rest_framework.decorators import api_view
from app.base.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


@api_view(['CREATE'])
def create(request):
    creating = EmployeeCreateSerializer(data=request.data)

    if not creating.is_valid():
        raise APIException({
            'detail': 'Invalid data',
            'errors': creating.errors,
        }, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    return Response({
        'detail': 'Created',
        'company': EmployeeExtendedSerializer(instance=creating.save()).data
    })


class EmployeeCrudView(APIView):
    http_method_names = ('get', 'update', 'delete',)

    def get(self, request, company_id):
        return Response({
            'detail': 'Found',
            'company': EmployeeExtendedSerializer(instance=Employee.get_by_id(company_id)).data,
        })

    def update(self, request, company_id):
        updating = EmployeeUpdateSerializer(instance=Employee.get_by_id(company_id), data=request.data)

        if not updating.is_valid():
            raise APIException({
                'detail': 'Invalid data',
                'errors': updating.errors,
            }, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

        return Response({
            'detail': 'Updated',
            'company': EmployeeExtendedSerializer(instance=updating.save()).data
        })

    def delete(self, request, company_id):
        return Response({
            'detail': 'Deleted',
            'deleted': Employee.get_by_id(company_id).delete(),
        })
