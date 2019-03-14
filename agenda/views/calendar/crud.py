from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from agenda.models import Calendar, get_calendar_by_id as _get_calendar


class CalendarActions(APIView):
    def post(self, request):
        validator = Calendar.validators.create(data=request.data)

        if not validator.validate():
            return Response({
                'detail': 'Invalid',
                'errors': validator.errors,
            })

        calendar = Calendar.model(**{k: v for k, v in validator.data.items() if v is not None})
        calendar.save()

        return Response(data={
            'detail': 'Calendar has been created',
            'calendar': Calendar.serializers.base(instance=calendar).data,
        }, status=status.HTTP_201_CREATED)

    def get(self, request, calendar_id):
        calendar = _get_calendar(calendar_id)

        return Response(data={
            'detail': 'Calendar has been found',
            'calendar': Calendar.serializers.base(instance=calendar).data,
        })

    def put(self, request, calendar_id):
        calendar = _get_calendar(calendar_id)
        validator = Calendar.validators.update(data=request.data)

        if not validator.validate():
            return Response({
                'detail': 'Invalid',
                'errors': validator.errors,
            })

        calendar.update(validator.data, nullable=False)

        return Response(data={
            'detail': 'Calendar has been updated',
            'calendar': Calendar.serializers.base(instance=calendar).data,
        })

    def delete(self, request, calendar_id):
        calendar = _get_calendar(calendar_id)
        calendar.delete()

        return Response(data={
            'detail': 'Calendar has been deleted',
            'calendar': Calendar.serializers.base(instance=calendar).data,
        })

    def restore(self, request, calendar_id):
        calendar = Calendar.model.deleted.get(pk=calendar_id)
        calendar.deleted_at = None
        calendar.save(force_update=True)

        return Response(data={
            'detail': 'Calendar has been restored',
            'calendar': Calendar.serializers.base(instance=calendar).data,
        })

    def purge(self, request, calendar_id):
        calendar = _get_calendar(calendar_id)
        calendar.hard_delete()

        return Response(data={
            'detail': 'Calendar has been purged',
            'calendar': Calendar.serializers.base(instance=calendar).data,
        })
