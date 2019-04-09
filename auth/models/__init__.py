# All imports here is for Django to see those models and for better use experience

from auth.models.user.model import User
from auth.models.user.serializers import UserSerializer, UserExtendedSerializer
from auth.models.user.admin import UserAdmin

from auth.models.feature.model import Feature
from auth.models.feature.serializers import FeatureSerializer
from auth.models.feature.admin import FeatureAdmin

from auth.models.progress.model import Progress
from auth.models.progress.serializers import ProgressSerializer


# Getters part

def get_user(user_id, raise_exception=True) -> User:
    from app.base.exceptions import NotFound

    user = User.objects.filter(pk=user_id).first()

    if not user and raise_exception:
        raise NotFound()

    return user


def get_feature(feature_id, raise_exception=True) -> Feature:
    from app.base.exceptions import NotFound

    feature = Feature.objects.filter(pk=feature_id).first()

    if not feature and raise_exception:
        raise NotFound()

    return feature
