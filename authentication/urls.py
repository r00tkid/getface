from django.urls import path
from authentication.views import auth, progress

from rest_framework_jwt.views import ObtainJSONWebToken, refresh_jwt_token
from authentication.jwt import CustomJWTSerializer

urlpatterns = [
    path('/me', auth.self_info),

    path('/sign-up', auth.sign_up),
    path('/worker', auth.worker_sign_up),
    path('/confirm', auth.activate_account),
    path('/sign-in', ObtainJSONWebToken.as_view(serializer_class=CustomJWTSerializer)),
    path('/fresh', refresh_jwt_token),
    path('/lost', auth.reset_password),
    path('/reset', auth.reset_confirm),

    path('/progress/<int:feature_id>', progress.add_progress),
    path('/progress/<int:feature_id>', progress.remove_progress),
]
