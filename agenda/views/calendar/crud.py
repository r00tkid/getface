from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from agenda.models import Calendar


class CalendarActions(APIView):
    def post(self, request):
        validator = Calendar.action()(data=request.data)

        if not validator.validate():
            return Response({
                'detail': 'Invalid',
                'errors': validator.errors,
            })

        calendar = Calendar.new({k: v for k, v in validator.data.items() if v is not None})
        calendar.save()

        return Response(data={
            'detail': 'Calendar has been created',
            'calendar': Calendar.serializer()(instance=calendar).data,
        }, status=status.HTTP_201_CREATED)

    def get(self, request, calendar_id):
        return Response(data={
            'detail': 'Calendar has been found',
            'calendar': Calendar.info(calendar_id).data,
        })

    def put(self, request, calendar_id):
        calendar = Calendar.info(calendar_id)
        validator = Calendar.action('update')(data=request.data)

        if not validator.validate():
            return Response({
                'detail': 'Invalid',
                'errors': validator.errors,
            })

        calendar.instance.update(validator.data, nullable=False)

        return Response(data={
            'detail': 'Calendar has been updated',
            'calendar': calendar.data,
        })

    def delete(self, request, calendar_id):
        calendar: Calendar.model() = Calendar.info(calendar_id).instance
        calendar.delete()

        return Response(data={
            'detail': 'Calendar has been deleted',
            'calendar': Calendar.serializer()(instance=calendar).data,
        })

    def restore(self, request, calendar_id):
        calendar = Calendar.model().deleted.get(pk=calendar_id)
        calendar.deleted_at = None
        calendar.save(force_update=True)

        return Response(data={
            'detail': 'Calendar has been restored',
            'calendar': Calendar.serializer()(instance=calendar).data,
        })

    def purge(self, request, calendar_id):
        calendar: Calendar.model() = Calendar.info(calendar_id).instance
        calendar.hard_delete()

        return Response(data={
            'detail': 'Calendar has been purged',
            'calendar': Calendar.serializer()(instance=calendar).data,
        })
