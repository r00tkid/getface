from index.base.repository import Base
from company.models import Worker


class Create(Base.Validator):
    field = Base.Validator.field
    valid = Base.Validator.valid

    start = field.DateTime("Начал", [
        valid.DataRequired()
    ])

    end = field.DateTime("Закончил", [
        valid.DataRequired()
    ])

    active = field.Integer("Активность", [
        valid.NotRequired(is_string=False),
        valid.NumberRange(min=0, max=100),
    ])

    mood = field.Integer("Настроение", [
        valid.NotRequired(is_string=False),
        valid.NumberRange(min=0, max=100),
    ])

    fatigue = field.Integer("Усталость", [
        valid.NotRequired(is_string=False),
        valid.NumberRange(min=0, max=100),
    ])

    worker_id = field.Integer("ID работника", [
        valid.ValidationChain(
            valid.DataRequired(),
            valid.NumberRange(min=1),
            valid.Exists(Worker.model(), 'id'),
        ),
    ])


class Update(Base.Validator):
    field = Base.Validator.field
    valid = Base.Validator.valid

    start = field.DateTime("Начал", [
        valid.NotRequired(allow_empty=False)
    ])

    end = field.DateTime("Закончил", [
        valid.NotRequired(allow_empty=False)
    ])

    active = field.Integer("Активность", [
        valid.NotRequired(is_string=False),
        valid.NumberRange(min=0, max=100),
    ])

    mood = field.Integer("Настроение", [
        valid.NotRequired(is_string=False),
        valid.NumberRange(min=0, max=100),
    ])

    fatigue = field.Integer("Усталость", [
        valid.NotRequired(is_string=False),
        valid.NumberRange(min=0, max=100),
    ])
