from django.urls import path
from tech import views

urlpatterns = [

    path('/sign-in', views.sign_in),
    path('/sign-up', views.sign_up),
    path('/worker-sign-up', views.worker_sign_up),

]
