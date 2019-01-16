__all__ = ['CanManageWorkers', 'WorkerActions']

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


class CanManageWorkers(IsAuthenticated):
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False

        data = request.parser_context.get('kwargs', {})
        user = request.user

        try:
            company = Company.objects.get(pk=data.get('company_id'))
        except:
            raise CompanyNotFound("Company with id:[%s] not found." % data.get('company_id'))

        if request.method not in ('POST', 'RESTORE'):
            try:
                Worker.objects.get(pk=data.get('worker_id'), company_id=data.get('company_id'))
            except:
                raise WorkerNotFound("Worker with id:[%s] not found." % data.get('worker_id'))

        if 'RESTORE' == request.method:
            try:
                Worker.all_objects.get(pk=data.get('worker_id'), company_id=data.get('company_id'))
            except:
                raise WorkerNotFound("Worker with id:[%s] not found." % data.get('worker_id'))

        manager = Worker.objects.filter(user=user, company_id=data.get('company_id')).first()

        is_owner = user.id == company.owner_id
        is_manager = manager and manager.is_manager and not manager.is_fired

        if not is_owner and not is_manager:
            raise NotAllowed()

        return True


class WorkerActions(APIView):
    # Change to CanManageWorkers
    permission_classes = (CanManageWorkers,)
    http_method_names = ['get', 'post', 'put', 'delete', 'restore', 'purge', 'fire', 'hire']

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
        worker = Worker.objects.get(pk=worker_id)

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
        worker = Worker.objects.get(pk=worker_id)

        worker.delete()

        return Response(data={
            'detail': 'Worker %s %s has been deleted' % (worker.first_name, worker.last_name),
            'worker': WorkerSerializer(instance=worker).data,
        })

    def restore(self, request, worker_id, company_id):
        worker = Worker.all_objects.get(pk=worker_id)

        worker.deleted_at = None
        worker.save()

        return Response({
            'detail': 'Worker %s %s has been restored' % (worker.first_name, worker.last_name),
            'worker': WorkerSerializer(instance=worker).data
        })

    def purge(self, request, worker_id, company_id):
        worker = Worker.objects.get(pk=worker_id)

        worker.hard_delete()

        return Response(data={
            'detail': 'Worker %s %s has been fully removed from system' % (worker.first_name, worker.last_name),
            'worker': WorkerSerializer(instance=worker).data,
        })

    def fire(self, request, worker_id, company_id):
        worker = Worker.objects.get(pk=worker_id)

        worker.is_fired = True
        worker.save()

        return Response({
            'detail': 'Worker has been fired',
            'worker': WorkerSerializer(instance=worker).data,
        })

    def hire(self, request, worker_id, company_id):
        worker = Worker.objects.get(pk=worker_id)

        worker.is_fired = False
        worker.save()

        return Response({
            'detail': 'Worker has been hired',
            'worker': WorkerSerializer(instance=worker).data,
        })
