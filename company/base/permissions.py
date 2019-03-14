from rest_framework.permissions import IsAuthenticated
from employee.models import Employee
from company.models import Company
from . import exceptions


class CanManageCompany(IsAuthenticated):
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False

        data = request.parser_context.get('kwargs', {})
        user = request.user

        if 'POST' != request.method or data.get('company_id', False):
            try:
                company = Company.model().objects.get(pk=data.get('company_id'))
            except:
                raise exceptions.CompanyNotFound("Company with id:[%s] not found." % data.get('company_id'))

            manager = Employee.model.objects.filter(user=user, company_id=data.get('company_id')).first()

            is_owner = user.id == company.owner_id
            is_manager = manager and manager.is_manager and not manager.is_fired

            if not is_owner and not is_manager:
                raise exceptions.NotAllowed()

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
                Employee.model().objects.get(pk=data.get('employee_id'), company_id=data.get('company_id'))
            except:
                raise exceptions.WorkerNotFound("Employee with id:[%s] not found." % data.get('employee_id'))

        if 'RESTORE' == request.method:
            if data.get('employee_id', 'no_data') is 'no_data':
                raise exceptions.NotFound

            try:
                Employee.model.all.get(pk=data.get('employee_id'), company_id=data.get('company_id'))
            except:
                raise exceptions.WorkerNotFound("Employee with id:[%s] not found." % data.get('employee_id'))

        return True
