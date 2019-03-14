from index.base.repository import Base
from employee.models import Employee


class CalendarCreateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    start = field.DateTime("Начало", [
        validation.DataRequired()
    ])

    end = field.DateTime("Конец", [
        validation.DataRequired()
    ])

    worker_id = field.Integer("Работник", [
        validation.ValidationChain(
            validation.DataRequired(),
            validation.NumberRange(min=1),
            validation.Exists(Employee.model(), 'id'),
        ),
    ])


class CalendarUpdateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    start = field.DateTime("Начало", [
        validation.NotRequired(allow_empty=False)
    ])

    end = field.DateTime("Конец", [
        validation.NotRequired(allow_empty=False)
    ])
