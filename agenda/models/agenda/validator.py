from index.base.repository import Base
from employee.models import Employee


class AgendaCreateValidator(Base.Validator):
    field = Base.Validator.field
    validation = Base.Validator.validation

    start = field.DateTime("Начал", [
        validation.DataRequired()
    ])

    end = field.DateTime("Закончил", [
        validation.DataRequired()
    ])

    active = field.Integer("Активность", [
        validation.NotRequired(is_string=False),
        validation.NumberRange(min=0, max=100),
    ])

    mood = field.Integer("Настроение", [
        validation.NotRequired(is_string=False),
        validation.NumberRange(min=0, max=100),
    ])

    fatigue = field.Integer("Усталость", [
        validation.NotRequired(is_string=False),
        validation.NumberRange(min=0, max=100),
    ])

    worker_id = field.Integer("ID работника", [
        validation.ValidationChain(
            validation.DataRequired(),
            validation.NumberRange(min=1),
            validation.Exists(Employee.model(), 'id'),
        ),
    ])


class AgendaUpdateValidator(Base.Validator):
    field = Base.Validator.field
    validation = Base.Validator.validation

    start = field.DateTime("Начал", [
        validation.NotRequired(allow_empty=False)
    ])

    end = field.DateTime("Закончил", [
        validation.NotRequired(allow_empty=False)
    ])

    active = field.Integer("Активность", [
        validation.NotRequired(is_string=False),
        validation.NumberRange(min=0, max=100),
    ])

    mood = field.Integer("Настроение", [
        validation.NotRequired(is_string=False),
        validation.NumberRange(min=0, max=100),
    ])

    fatigue = field.Integer("Усталость", [
        validation.NotRequired(is_string=False),
        validation.NumberRange(min=0, max=100),
    ])
