__all__ = ('WorkerActions',)

import uuid
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from company.models import Worker
from company.serializers import WorkerSerializer
from company.base.permissions import CanManageWorkers
from authentication.models import get_user_model

User = get_user_model()


class WorkerActions(APIView):
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

        worker = Worker.objects.get(pk=worker_id).update(validator.data, nullable=False)

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
