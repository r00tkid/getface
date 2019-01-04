from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='posts.index'),
    path('<int:post_id>', views.one, name='posts.one'),
    path('fake/<int:amount>', views.fake, name='posts.fake'),
]
