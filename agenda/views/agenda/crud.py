from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from agenda.models import Agenda


class AgendaActions(APIView):
    http_method_names = ['get', 'post', 'put', 'delete', 'restore', 'purge']

    def post(self, request):
        validator = Agenda.action()(data=request.data)

        if not validator.validate():
            return Response({
                'detail': 'Invalid',
                'errors': validator.errors,
            })

        agenda = Agenda.new({k: v for k, v in validator.data.items() if v is not None})
        agenda.save()

        return Response(data={
            'detail': 'Agenda has been created',
            'agenda': Agenda.serializer()(instance=agenda).data,
        }, status=status.HTTP_201_CREATED)

    def get(self, request, agenda_id):
        return Response(data={
            'detail': 'Agenda has been found',
            'agenda': Agenda.info(agenda_id).data,
        })

    def put(self, request, agenda_id):
        agenda = Agenda.info(agenda_id)
        validator = Agenda.action('update')(data=request.data)

        if not validator.validate():
            return Response({
                'detail': 'Invalid',
                'errors': validator.errors,
            })

        agenda.instance.update(validator.data, nullable=False)

        return Response(data={
            'detail': 'Agenda has been updated',
            'agenda': agenda.data,
        })

    def delete(self, request, agenda_id):
        agenda: Agenda.model() = Agenda.info(agenda_id).instance
        agenda.delete()

        return Response(data={
            'detail': 'Agenda has been deleted',
            'agenda': Agenda.serializer()(instance=agenda).data,
        })

    def restore(self, request, agenda_id):
        agenda = Agenda.model().deleted.get(pk=agenda_id)
        agenda.deleted_at = None
        agenda.save(force_update=True)

        return Response(data={
            'detail': 'Agenda has been restored',
            'agenda': Agenda.serializer()(instance=agenda).data,
        })

    def purge(self, request, agenda_id):
        agenda: Agenda.model() = Agenda.info(agenda_id).instance
        agenda.hard_delete()

        return Response(data={
            'detail': 'Agenda has been purged',
            'agenda': Agenda.serializer()(instance=agenda).data,
        })
