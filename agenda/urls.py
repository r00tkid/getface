from django.urls import path
from agenda.views.agenda.crud import AgendaActions
from agenda.views.calendar.crud import CalendarActions

urlpatterns = [
    path('/agenda', AgendaActions.as_view()),
    path('/time', CalendarActions.as_view()),
]
