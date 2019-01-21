from django.urls import path, include
from tech import views

urlpatterns = [

    path('/form', include('tech.urls.form')),
    path('/check-validator', views.check_checker)

]
