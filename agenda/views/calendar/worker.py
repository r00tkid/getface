from dateutil import parser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from employee.models import Employee
from agenda.models import Calendar, Agenda


@api_view(('POST',))
def want_to_work(request):
    employee = Employee.info(request.data.get('employee_id'))

    if request.user.id != employee.instance.user_id:
        return Response({
            'detail': 'Access forbidden',
        }, status=status.HTTP_403_FORBIDDEN)

    calendar = Calendar.info(request.data.get('calendar_id'))

    if calendar.instance.employee_id != employee.instance.id:
        return Response({
            'detail': 'This calendar not for you',
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    calendar.instance.is_wanted = bool(request.data.get('wanted'))
    calendar.instance.save(force_update=True)

    return Response({
        'detail': 'Status changed',
        'calendar': calendar.data,
    })


@api_view(('POST',))
def get_own_agenda(request):
    employee = Employee.info(request.data.get('employee_id'))

    if request.user.id != employee.instance.user_id:
        return Response({
            'detail': 'Access forbidden',
        }, status=status.HTTP_403_FORBIDDEN)

    start = parser.parse(request.data.get('start'))
    end = parser.parse(request.data.get('end'))

    # todo: do

    calendar = Calendar.model().objects.filter(
        employee=employee.instance,
        start__year=start.year,
        start__day=start.day,
        end__year=end.year,
        end__day=end.day,
    )

    agenda = Agenda.model().objects.filter(
        employee=employee.instance,
        start__year=start.year,
        start__day=start.day,
        end__year=end.year,
        end__day=end.day,
    )

    return Response({
        'calendar': Calendar.serializer()(instance=calendar, many=True).data,
        'agenda': Agenda.serializer()(instance=agenda, many=True).data,
    })
