import uuid
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from company.base.permissions import CanManageWorkers
from company.models import Worker
from authentication.models import User


class WorkerActions(APIView):
    permission_classes = (CanManageWorkers,)
    http_method_names = ['get', 'post', 'invite', 'faceid', 'put', 'delete', 'restore', 'purge', 'fire', 'hire']

    def post(self, request, company_id):
        validator = Worker.action('create')(data=request.data)

        if not validator.validate():
            return Response({
                'detail': 'Form not valid',
                'errors': validator.errors,
            })

        data = validator.data

        try:
            worker = Worker.model().objects.get(email=data.get('email'), company_id=company_id)

            return Response({
                'detail': 'Worker with current mail already exists in your company',
                'worker': Worker.serializer()(instance=worker).data,
            }, status=status.HTTP_207_MULTI_STATUS)
        except:
            pass

        worker = Worker.new({
            'first_name': data.get('first_name'),
            'last_name': data.get('last_name'),
            'email': data.get('email'),
            'phone': data.get('phone') if data.get('phone') and data.get('phone') != '' else None,
            'company_id': company_id,
        })

        try:
            user = User.model().objects.get(email=data.get('email'))

            worker.user_id = user.id
        except:
            user = User.new({
                'username': uuid.uuid4(),
                'email': data.get('email'),
                'first_name': data.get('first_name'),
                'last_name': data.get('last_name'),
                'is_active': False,
            })

            user.set_password(user.username)
            user.save()

        # In first place I was thinking to send mail on creating, but than mechanics has change
        worker.save()

        return Response(data={
            'detail': 'Worker has been created',
            'worker': Worker.serializer('extended')(instance=worker).data,
        }, status=status.HTTP_201_CREATED)

    def invite(self, request, worker_id, company_id):
        data: dict = request.data
        s_worker = Worker.info(pk=worker_id)
        o_worker: Worker.model() = s_worker.instance

        if o_worker.is_active:
            return Response({
                'detail': 'Worker activated already'
            }, status=status.HTTP_409_CONFLICT)

        previous_invitation = o_worker.new_invitation()
        o_worker.is_invited = True
        o_worker.save()

        return Response({
            'detail': 'Worker has been invited',
            'previous_invitation': previous_invitation,
        })

    def faceid(self, request, worker_id, company_id):
        data: dict = request.data
        s_worker = Worker.info(pk=worker_id)
        o_worker: Worker.model() = s_worker.instance

        if data.get('remove'):
            o_worker.clear_face_id()
            o_worker.save()

            return Response({
                'detail': 'Worker face-id has been removed.'
            })

        o_worker.new_face_id()
        o_worker.save()

        return Response({
            'detail': 'Worker face-id has been updated',
            'face_id': o_worker.face_id,
        })

    def get(self, request, worker_id, company_id):
        options = request.GET

        if options.get('all') != '':
            worker = Worker.model().objects
        else:
            worker = Worker.model().all

        try:
            return Response({
                'detail': 'Worker has been found',
                'worker': Worker.serializer('extended')(instance=worker.get(id=worker_id)).data
            })
        except:
            return Response(data={
                'detail': 'Worker has not been found',
            }, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, worker_id, company_id):
        validator = Worker.action('update')(data=request.data)

        if not validator.validate():
            return Response({
                'detail': 'Your data is invalid',
                'errors': validator.errors,
            })

        worker = Worker.model().objects.get(pk=worker_id).update(validator.data, nullable=False)

        return Response(data={
            'detail': 'Worker has been updated',
            'worker': Worker.serializer('extended')(instance=worker).data,
        })

    def delete(self, request, worker_id, company_id):
        worker = Worker.model().objects.get(pk=worker_id)

        worker.delete()

        return Response(data={
            'detail': 'Worker %s %s has been deleted' % (worker.first_name, worker.last_name),
            'worker': Worker.serializer('extended')(instance=worker).data,
        })

    def restore(self, request, worker_id, company_id):
        worker = Worker.model().deleted.get(pk=worker_id)

        worker.deleted_at = None
        worker.save()

        return Response({
            'detail': 'Worker %s %s has been restored' % (worker.first_name, worker.last_name),
            'worker': Worker.info('extended')(instance=worker).data
        })

    def purge(self, request, worker_id, company_id):
        worker = Worker.model().objects.get(pk=worker_id)

        worker.hard_delete()

        return Response(data={
            'detail': 'Worker %s %s has been fully removed from system' % (worker.first_name, worker.last_name),
            'worker': Worker.serializer('extended')(instance=worker).data,
        })

    def fire(self, request, worker_id, company_id):
        worker = Worker.model().objects.get(pk=worker_id)

        worker.is_fired = True
        worker.save()

        return Response({
            'detail': 'Worker has been fired',
            'worker': Worker.serializer('extended')(instance=worker).data,
        })

    def hire(self, request, worker_id, company_id):
        worker = Worker.model().objects.get(pk=worker_id)

        worker.is_fired = False
        worker.save()

        return Response({
            'detail': 'Worker has been hired',
            'worker': Worker.serializer('extended')(instance=worker).data,
        })
