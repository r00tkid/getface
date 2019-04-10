from rest_framework_jwt.views import ObtainJSONWebToken, refresh_jwt_token
from entry.jwt import CustomJWTSerializer
from entry.views import auth, progress
from django.urls import path

urlpatterns = [
    path('/me', auth.self_info),

    path('/sign-up', auth.sign_up),
    path('/worker', auth.employee_sign_up),
    path('/confirm', auth.activate_account),

    # Base jwt paths
    path('/sign-in', ObtainJSONWebToken.as_view(serializer_class=CustomJWTSerializer)),
    path('/refresh', refresh_jwt_token),

    path('/resend', auth.resend_mail_invitation),
    path('/lost', auth.reset_password),
    path('/reset', auth.reset_confirm),

    path('/progress/<int:feature_id>', progress.add_progress),
    path('/progress/<int:feature_id>', progress.remove_progress),
]
