from agenda.models.agenda.model import Agenda as AgendaModel
from agenda.models.calendar.model import Calendar as CalendarModel

from agenda.models.agenda.repository import Repository as Agenda
from agenda.models.calendar.repository import Repository as Calendar


def get_agenda_by_id(agenda_id, raise_exception=True) -> Agenda.model():
    from index.base.exceptions import APIException

    agenda = Agenda.model.objects.filter(pk=agenda_id).first()

    if not agenda and raise_exception:
        raise APIException({
            'detail': 'Agenda not found'
        }, status_code=404)

    return agenda


def get_calendar_by_id(calendar_id, raise_exception=True) -> Calendar.model():
    from index.base.exceptions import APIException

    calendar = Calendar.model.objects.filter(pk=calendar_id).first()

    if not calendar and raise_exception:
        raise APIException({
            'detail': 'Calendar not found'
        }, status_code=404)

    return calendar
