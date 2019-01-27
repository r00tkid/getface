from index.base.repository import Base
from authentication.models import User, Feature


class Create(Base.Validator):
    field = Base.Validator.field
    valid = Base.Validator.valid

    user_id = field.Integer("User", [
        valid.Exists(
            User.model(),
            'pk',
            'User not found'
        )
    ])

    feature_id = field.Integer("Feature", [
        valid.Exists(
            Feature.model(),
            'pk',
            'Feature not found'
        )
    ])
