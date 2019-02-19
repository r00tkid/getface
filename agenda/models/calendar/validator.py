from index.base.repository import Base
from employee.models import Employee


class Create(Base.Validator):
    field = Base.Validator.field
    valid = Base.Validator.valid

    start = field.DateTime("Начало", [
        valid.DataRequired()
    ])

    end = field.DateTime("Конец", [
        valid.DataRequired()
    ])

    worker_id = field.Integer("Работник", [
        valid.ValidationChain(
            valid.DataRequired(),
            valid.NumberRange(min=1),
            valid.Exists(Employee.model(), 'id'),
        ),
    ])


class Update(Base.Validator):
    field = Base.Validator.field
    valid = Base.Validator.valid

    start = field.DateTime("Начало", [
        valid.NotRequired(allow_empty=False)
    ])

    end = field.DateTime("Конец", [
        valid.NotRequired(allow_empty=False)
    ])
