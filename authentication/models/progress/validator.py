from authentication.models.feature.model import Feature
from authentication.models.user.model import User
from index.base.repository import Base


class ProgressCreateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    user_id = field.integer("User", [
        validation.exists(
            User,
            'pk',
            'User not found'
        )
    ])

    feature_id = field.integer("Feature", [
        validation.exists(
            Feature,
            'pk',
            'Feature not found'
        )
    ])
