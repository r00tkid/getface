__all__ = ('CompanyActions',)

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from company.base.permissions import CanManageCompany
from company.models import Company
from company.serializers import CompanySerializer, CompanyFullInfoSerializer


class CompanyActions(APIView):
    permission_classes = (CanManageCompany,)
    http_method_names = ['get', 'post', 'put', 'delete', 'restore', 'purge']

    def post(self, request):
        from form.modules.company import RegisterCompany
        validator = RegisterCompany(data=request.data)

        if not validator.validate():
            return Response({
                'detail': 'Data is invalid',
                'errors': validator.errors,
            }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        company = Company(**validator.data)
        company.owner_id = request.user.id

        return Response(data={
            'detail': 'Company has been created',
            'company': CompanySerializer(instance=company).data,
        }, status=status.HTTP_201_CREATED)

    def get(self, request, company_id):
        return Response({
            'detail': 'Company info',
            'company': CompanyFullInfoSerializer(
                instance=Company.all_objects.get(
                    pk=company_id
                ) if request.GET.get('all') == '' else Company.objects.get(
                    pk=company_id
                )
            )
        })

    def put(self, request, company_id):
        from form.modules.company import UpdateCompany
        validator = UpdateCompany(data=request.data)

        if not validator.validate():
            return Response({
                'detail': 'Data is invalid',
                'errors': validator.errors,
            }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        company = Company.objects.get(pk=company_id).update(validator.data, nullable=False)

        return Response(data={
            'detail': 'Company view',
            'company': CompanyFullInfoSerializer(instance=company).data,
        })

    def delete(self, request, company_id):
        company = Company.objects.get(pk=company_id)
        company.delete()

        return Response(data={
            'detail': 'Company has been deleted',
            'company': CompanySerializer(instance=company).data,
        })

    def restore(self, request, company_id):
        company = Company.objects.get(pk=company_id)
        company.deleted_at = None

        return Response(data={
            'detail': 'Company has been restored',
            'company': CompanySerializer(instance=company).data,
        })

    def purge(self, request, company_id):
        company = Company.objects.get(pk=company_id)
        company.hard_delete()

        return Response(data={
            'detail': 'Company has been purged',
            'company': CompanySerializer(instance=company).data,
        })
