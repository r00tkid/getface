from authentication.models.user.model import User as UserModel
from authentication.models.feature.model import Feature as FeatureModel
from authentication.models.progress.model import Progress as ProgressModel

from authentication.models.user.repository import Repository as User
from authentication.models.feature.repository import Repository as Feature
from authentication.models.progress.repository import Repository as Progress


def get_user_by_id(user_id, raise_exception=True) -> User.model():
    from index.base.exceptions import APIException

    user = User.model.objects.filter(pk=user_id).first()

    if not user and raise_exception:
        raise APIException({
            'detail': 'User not found'
        }, status_code=404)

    return user


def get_feature_by_id(feature_id, raise_exception=True) -> Feature.model():
    from index.base.exceptions import APIException

    feature = Feature.model.objects.filter(pk=feature_id).first()

    if not feature and raise_exception:
        raise APIException({
            'detail': 'Feature not found'
        }, status_code=404)

    return feature
