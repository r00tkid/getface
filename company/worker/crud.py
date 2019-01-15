__all__ = ['CanManageCompany', 'WorkerCrud']

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from company.models import Worker, Company
from company.serializers import WorkerSerializer
from authentication.serializers import User
import uuid


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
        from form.modules.worker import CreateWorker
        validator = CreateWorker(data=request.data)

        if not validator.validate():
            return Response({
                'detail': 'Form not valid',
                'errors': validator.errors,
            })

        data = validator.data

        try:
            worker = Worker.objects.get(email=data.get('email'), company_id=company_id)

            return Response({
                'detail': 'Worker with current mail already exists in your company',
                'worker': WorkerSerializer(instance=worker).data,
            }, status=status.HTTP_207_MULTI_STATUS)
        except:
            pass

        worker = Worker(**{
            'first_name': data.get('first_name'),
            'last_name': data.get('last_name'),
            'email': data.get('email'),
            'phone': data.get('phone') if data.get('phone') and data.get('phone') != '' else None,
            'company_id': company_id,
        })

        try:
            user = User.objects.get(email=data.get('email'))

            worker.user_id = user.id
        except:
            user = User(**{
                'username': uuid.uuid4(),
                'email': data.get('email'),
                'first_name': data.get('first_name'),
                'last_name': data.get('last_name'),
                'is_active': False,
            })

            user.set_password(user.username)
            user.save()

        worker.save()

        return Response(data={
            'detail': 'Worker has been created',
            'worker': WorkerSerializer(instance=worker).data,
        }, status=status.HTTP_201_CREATED)

    def get(self, request, worker_id, company_id):
        options = request.GET

        if options.get('all') != '':
            worker = Worker.objects
        else:
            worker = Worker.all_objects

        try:
            return Response({
                'detail': 'Worker has been found',
                'worker': WorkerSerializer(instance=worker.get(id=worker_id)).data
            })
        except:
            return Response(data={
                'detail': 'Worker has not been found',
            }, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, worker_id, company_id):
        from form.modules.worker import UpdateWorker
        validator = UpdateWorker(data=request.data)

        if not validator.validate():
            return Response({
                'detail': 'Your data is invalid',
                'errors': validator.errors,
            })

        data = {k: v for k, v in validator.data.items() if v is not None}
        worker = Worker.objects.get(id=worker_id)

        if data.__len__() < 1:
            return Response({
                'detail': 'Worker has not been updated, cause there is nothing to update.',
                'worker': WorkerSerializer(instance=worker).data,
            })

        [worker.__setattr__(k, v) for k, v in data.items()]
        worker.save()

        return Response(data={
            'detail': 'Worker has been updated',
            'worker': WorkerSerializer(instance=worker).data,
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
