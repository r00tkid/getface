from index.base.repository import Base
from company.models import Worker


class Create(Base.Validator):
    field = Base.Validator.field
    valid = Base.Validator.valid

    start = field.DateTime(
        valid.DataRequired()
    )

    end = field.DateTime(
        valid.DataRequired()
    )

    active = field.Integer(
        valid.NotRequired(is_string=False),
        valid.NumberRange(min=0, max=100),
    )

    mood = field.Integer(
        valid.NotRequired(is_string=False),
        valid.NumberRange(min=0, max=100),
    )

    fatigue = field.Integer(
        valid.NotRequired(is_string=False),
        valid.NumberRange(min=0, max=100),
    )

    worker_id = field.Integer(
        valid.ValidationChain(
            valid.DataRequired(),
            valid.NumberRange(min=1),
            valid.Exists(Worker.model(), 'id'),
        ),
    )
