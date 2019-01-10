from django.urls import path
from . import views

from rest_framework_jwt.views import ObtainJSONWebToken, refresh_jwt_token
from .jwt import CustomJWTSerializer

urlpatterns = [
    path('self-info', views.self_info),

    path('sign-up', views.sign_up),
    path('worker', views.worker_sign_up),
    path('sign-in', ObtainJSONWebToken.as_view(serializer_class=CustomJWTSerializer)),
    path('fresh', refresh_jwt_token),
    path('lost', views.reset_password),
    path('reset', views.reset_confirm),
]
