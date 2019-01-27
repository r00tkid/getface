from django.urls import path
from agenda.views.agenda import crud as agenda
from agenda.views.calendar import crud as calendar, worker as calendar_worker

urlpatterns = [
    path('/calendar', calendar.CalendarActions.as_view()),
    path('/calendar/<int:calendar_id>', calendar.CalendarActions.as_view()),
    path('/agenda', agenda.AgendaActions.as_view()),
    path('/agenda/<int:agenda_id>', agenda.AgendaActions.as_view()),

    path('/calendar/wanted', calendar_worker.want_to_work),
    path('/calendar/own', calendar_worker.get_own_agenda)
]
