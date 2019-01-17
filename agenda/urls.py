from django.urls import path
from agenda.views import agenda, face

urlpatterns = [
    path('/agenda', agenda.AgendaActions.as_view()),
    path('/time', face.FaceTimeActions.as_view()),
]
