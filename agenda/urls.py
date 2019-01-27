from django.urls import path
from agenda.views.agenda.crud import AgendaActions
from agenda.views.calendar.crud import CalendarActions

urlpatterns = [
    path('/calendar', CalendarActions.as_view()),
    path('/calendar/<int:calendar_id>', CalendarActions.as_view()),
    path('/agenda', AgendaActions.as_view()),
    path('/agenda/<int:agenda_id>', AgendaActions.as_view()),
]
