from rest_framework.permissions import IsAuthenticated
from company.models import Worker, Company
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

            manager = Worker.model().objects.filter(user=user, company_id=data.get('company_id')).first()

            is_owner = user.id == company.owner_id
            is_manager = manager and manager.is_manager and not manager.is_fired

            if not is_owner and not is_manager:
                raise exceptions.NotAllowed()

        return True


class CanManageWorkers(CanManageCompany):
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False

        data = request.parser_context.get('kwargs', {})

        if request.method not in ('POST', 'RESTORE'):
            if data.get('worker_id', 'no_data') is 'no_data':
                raise exceptions.NotFound

            try:
                Worker.model().objects.get(pk=data.get('worker_id'), company_id=data.get('company_id'))
            except:
                raise exceptions.WorkerNotFound("Worker with id:[%s] not found." % data.get('worker_id'))

        if 'RESTORE' == request.method:
            if data.get('worker_id', 'no_data') is 'no_data':
                raise exceptions.NotFound

            try:
                Worker.model().all_objects.get(pk=data.get('worker_id'), company_id=data.get('company_id'))
            except:
                raise exceptions.WorkerNotFound("Worker with id:[%s] not found." % data.get('worker_id'))

        return True
