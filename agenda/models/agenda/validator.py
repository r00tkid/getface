from index.base.repository import Base
from employee.models import Employee


class AgendaCreateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    start = field.date_time("Начал", [
        validation.data_required()
    ])

    end = field.date_time("Закончил", [
        validation.data_required()
    ])

    active = field.integer("Активность", [
        validation.not_required(is_string=False),
        validation.number_range(min=0, max=100),
    ])

    mood = field.integer("Настроение", [
        validation.not_required(is_string=False),
        validation.number_range(min=0, max=100),
    ])

    fatigue = field.integer("Усталость", [
        validation.not_required(is_string=False),
        validation.number_range(min=0, max=100),
    ])

    worker_id = field.integer("ID работника", [
        validation.validation_chain(
            validation.data_required(),
            validation.number_range(min=1),
            validation.exists(Employee.model(), 'id'),
        ),
    ])


class AgendaUpdateValidator(Base.Validator):
    field = Base.Validator.field
    validation = Base.Validator.validation

    start = field.date_time("Начал", [
        validation.not_required(allow_empty=False)
    ])

    end = field.date_time("Закончил", [
        validation.not_required(allow_empty=False)
    ])

    active = field.integer("Активность", [
        validation.not_required(is_string=False),
        validation.number_range(min=0, max=100),
    ])

    mood = field.integer("Настроение", [
        validation.not_required(is_string=False),
        validation.number_range(min=0, max=100),
    ])

    fatigue = field.integer("Усталость", [
        validation.not_required(is_string=False),
        validation.number_range(min=0, max=100),
    ])
