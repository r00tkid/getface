from django.urls import path, include
from tech import views

urlpatterns = [

    path('/form', include('tech.urls.form')),
    path('/turtle', views.turtle),
    path('/fortune', views.fortune),

    path('/user/<int:user_id>', views.user_data_ext),
    path('/user/<int:user_id>/companies', views.user_data_companies),

]
