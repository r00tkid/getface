from holding.models import Company, Employee, Department, CompanyCreateSerializer, CompanyUpdateSerializer, CompanyExtendedSerializer
from rest_framework.decorators import api_view
from app.base.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


@api_view(['CREATE'])
def create(request):
    if request.headers.get('Example', False):
        return Response({
            'detail': 'Company creation path',
            'fields': CompanyCreateSerializer.fields_info(),
        })

    creating = CompanyCreateSerializer(data=request.data)

    if not creating.is_valid():
        raise APIException({
            'detail': 'Invalid data',
            'errors': creating.errors,
        }, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    owner = Employee.create_from_user(user=request.user)

    # Save company instance and add employee created from user as new owner
    company = creating.save(owner=owner)

    # Do not inline on owner position and department assigment
    department = Department(name='Топ менеджмент', company=company, is_protected=True)
    position = department.create_position(name='Владелец', is_protected=True)

    owner.set_position(position)
    owner.save()

    return Response({
        'detail': 'Created',
        'company': CompanyExtendedSerializer(instance=company).data,
    })


class CompanyCrudView(APIView):
    http_method_names = ('get', 'update', 'delete',)

    def get(self, request, pk):
        return Response({
            'detail': 'Found',
            'company': CompanyExtendedSerializer(instance=Company.get_by_id(pk)).data,
        })

    def update(self, request, pk):
        if request.headers.get('Example', False):
            return Response({
                'detail': 'Company update path',
                'fields': CompanyUpdateSerializer.fields_info(),
                'route_params': ('company primary key',),
            })

        updating = CompanyUpdateSerializer(instance=Company.get_by_id(pk), data=request.data)

        if not updating.is_valid():
            raise APIException({
                'detail': 'Invalid data',
                'errors': updating.errors,
            }, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

        return Response({
            'detail': 'Updated',
            'company': CompanyExtendedSerializer(instance=updating.save()).data
        })

    def delete(self, request, pk):
        return Response({
            'detail': 'Deleted',
            'deleted': Company.get_by_id(pk).delete(),
        })
