from django.urls import path, include
from . import views

urlpatterns = [

    path('sign-in', views.sign_in),
    path('sign-up', views.sign_up),

]
