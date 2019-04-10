from rest_framework.permissions import IsAuthenticated
from holding.models import Company, Employee
from app.base import exceptions


class CanManageCompany(IsAuthenticated):
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False

        data = request.parser_context.get('kwargs', {})
        user = request.user

        if 'POST' != request.method or data.get('company_id', False):
            company = Company.get_by_id(data.get('company_id'))
            manager = Employee.objects.filter(user=user, company=company).first()

            is_owner = user.id == company.owner_id
            is_manager = manager and manager.is_manager and not manager.is_fired

            if not is_owner and not is_manager:
                raise exceptions.APIException({}, 403)

        return True


class CanManageEmployees(CanManageCompany):
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False

        data = request.parser_context.get('kwargs', {})

        if request.method not in ('POST', 'RESTORE'):
            if data.get('employee_id', 'no_data') is 'no_data':
                raise exceptions.NotFound

            try:
                Employee.objects.get(pk=data.get('employee_id'), company_id=data.get('company_id'))
            except:
                raise exceptions.APIException({
                    'detail': "Employee with id:[%s] not found or company is wrong." % data.get('employee_id'),
                }, 404)

        if 'RESTORE' == request.method:
            if data.get('employee_id', 'no_data') is 'no_data':
                raise exceptions.NotFound

            try:
                Employee.all.get(pk=data.get('employee_id'), company_id=data.get('company_id'))
            except:
                raise exceptions.APIException({
                    'detail': "Employee with id:[%s] not found." % data.get('employee_id'),
                }, 404)

        return True
