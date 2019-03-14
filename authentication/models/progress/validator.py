from index.base.repository import Base
from authentication.models.user.model import User
from authentication.models.feature.model import Feature


class ProgressCreateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    user_id = field.Integer("User", [
        validation.Exists(
            User,
            'pk',
            'User not found'
        )
    ])

    feature_id = field.Integer("Feature", [
        validation.Exists(
            Feature,
            'pk',
            'Feature not found'
        )
    ])
