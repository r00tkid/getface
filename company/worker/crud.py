__all__ = ['CanManageCompany', 'WorkerCrud']

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from company.models import Worker, Company


class CompanyNotFound(APIException):
    status_code = 404
    default_detail = 'Specified company not found'


class WorkerNotFound(APIException):
    status_code = 404
    default_detail = 'Specified worker not found'


class NotAllowed(APIException):
    status_code = 403
    default_detail = 'You have no permissions to do this action'


class CanManageCompany(IsAuthenticated):
    def has_permission(self, request, view):
        if not super(CanManageCompany, self).has_permission(request, view):
            return False

        data = request.parser_context.get('kwargs', {})
        user = request.user

        try:
            company = Company.objects.get(pk=data.get('company_id'))
        except:
            raise CompanyNotFound("Company with id:[%s] not found." % data.get('company_id'))

        if 'POST' != request.method:
            try:
                Worker.objects.get(pk=data.get('worker_id'), company_id=data.get('company_id'))
            except:
                raise WorkerNotFound("Worker with id:[%s] not found." % data.get('worker_id'))

        manager = Worker.objects.filter(user=user, company_id=data.get('company_id')).first()

        if user.id != company.owner_id and (not manager or not manager.is_manager or manager.is_fired):
            raise NotAllowed()

        return True


class WorkerCrud(APIView):
    # Change to CanManageWorkers
    permission_classes = (CanManageCompany,)
    http_method_names = ['get', 'post', 'put', 'delete', 'purge']

    def post(self, request, company_id):
        return Response(data={
            'detail': 'Create worker',
            'method': request.method,
        }, status=status.HTTP_201_CREATED)

    def get(self, request, worker_id, company_id):
        return Response(data={
            'detail': 'Get [%s] worker' % worker_id,
            'method': request.method,
        })

    def put(self, request, worker_id, company_id):
        return Response(data={
            'detail': 'Update [%s] worker' % worker_id,
            'method': request.method,
        })

    def delete(self, request, worker_id, company_id):
        return Response(data={
            'detail': 'Soft delete [%s] worker' % worker_id,
            'method': request.method,
        })

    def purge(self, request, worker_id, company_id):
        return Response(data={
            'detail': 'Hard delete [%s] worker' % worker_id,
            'method': request.method,
        })
