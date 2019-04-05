from company.models import Company, get_company_by_id as _get_company
from company.base.permissions import CanManageCompany
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class CompanyActions(APIView):
    permission_classes = (CanManageCompany,)
    http_method_names = ['get', 'post', 'put', 'delete', 'restore', 'purge']

    def post(self, request):
        validator = Company.validators.create(data=request.data)

        if not validator.validate():
            return Response({
                'detail': 'Data is invalid',
                'errors': validator.errors,
            }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        company = Company.model(**validator.data)
        company.owner_id = request.user.id
        company.save()

        return Response(data={
            'detail': 'Company has been created',
            'company': Company.serializers.extended(instance=company).data,
        }, status=status.HTTP_201_CREATED)

    def get(self, request, company_id):
        company = _get_company(company_id)
        info = Company.serializers.extended(instance=company)

        info.add_owner()
        info.add_workers()

        return Response({
            'detail': 'Company info',
            'company': info.data,
        })

    def put(self, request, company_id):
        validator = Company.validators.update(data=request.data)

        if not validator.validate():
            return Response({
                'detail': 'Data is invalid',
                'errors': validator.errors,
            }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        company = Company.model().objects.get(pk=company_id)
        company.update(validator.data, nullable=False)
        info = Company.serializers.extended(instance=company)

        info.add_owner()
        info.add_workers()

        return Response(data={
            'detail': 'Company view',
            'company': info.data,
        })

    def delete(self, request, company_id):
        company = Company.model().objects.get(pk=company_id)
        company.delete()

        return Response(data={
            'detail': 'Company has been deleted',
            'company': Company.serializers.extended(instance=company).data,
        })

    def restore(self, request, company_id):
        company = Company.model().objects.get(pk=company_id)
        company.deleted_at = None

        return Response(data={
            'detail': 'Company has been restored',
            'company': Company.serializers.extended(instance=company).data,
        })

    def purge(self, request, company_id):
        company = Company.model().objects.get(pk=company_id)
        company.hard_delete()

        return Response(data={
            'detail': 'Company has been purged',
            'company': Company.serializers.extended(instance=company).data,
        })
