from dateutil import parser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from employee.models import Employee, get_employee_by_id as _get_employee
from agenda.models import Calendar, Agenda, get_calendar_by_id as _get_calendar


@api_view(('POST',))
def want_to_work(request):
    employee = _get_employee(request.data.get('employee_id'))

    if request.user.id != employee.user_id:
        return Response({
            'detail': 'Access forbidden',
        }, status=status.HTTP_403_FORBIDDEN)

    calendar = _get_calendar(request.data.get('calendar_id'))

    if calendar.employee_id != employee.id:
        return Response({
            'detail': 'This calendar not for you',
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    calendar.is_wanted = bool(request.data.get('wanted'))
    calendar.save(force_update=True)

    return Response({
        'detail': 'Status changed',
        'calendar': Calendar.serializers.base(instance=calendar).data,
    })


@api_view(('POST',))
def get_own_agenda(request):
    employee = _get_employee(request.data.get('employee_id'))

    if request.user.id != employee.user_id:
        return Response({
            'detail': 'Access forbidden',
        }, status=status.HTTP_403_FORBIDDEN)

    start = parser.parse(request.data.get('start'))
    end = parser.parse(request.data.get('end'))

    # todo: do

    calendar = Calendar.model().objects.filter(
        employee=employee,
        start__year=start.year,
        start__day=start.day,
        end__year=end.year,
        end__day=end.day,
    )

    agenda = Agenda.model().objects.filter(
        employee=employee,
        start__year=start.year,
        start__day=start.day,
        end__year=end.year,
        end__day=end.day,
    )

    return Response({
        'calendar': Calendar.serializers.base(instance=calendar, many=True).data,
        'agenda': Agenda.serializers.base(instance=agenda, many=True).data,
    })
