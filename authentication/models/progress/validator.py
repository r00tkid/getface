from index.base.repository import Base
from authentication.models.user.model import User
from authentication.models.feature.model import Feature


class Create(Base.Validator):
    field = Base.Validator.field
    valid = Base.Validator.valid

    user_id = field.Integer("User", [
        valid.Exists(
            User,
            'pk',
            'User not found'
        )
    ])

    feature_id = field.Integer("Feature", [
        valid.Exists(
            Feature,
            'pk',
            'Feature not found'
        )
    ])
