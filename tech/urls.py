from django.urls import path, include
from tech import views

form_patterns = [
    path('/sign-in', views.sign_in),
    path('/sign-up', views.sign_up),
    path('/worker-sign-up', views.worker_sign_up),
]

urlpatterns = [

    path('/form', include('tech.urls.form_patterns')),
    path('/check-validator', views.check_checker)

]
