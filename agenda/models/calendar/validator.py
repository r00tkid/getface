from index.base.repository import Base
from employee.models import Employee


class CalendarCreateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    start = field.date_time("Начало", [
        validation.data_required()
    ])

    end = field.date_time("Конец", [
        validation.data_required()
    ])

    worker_id = field.integer("Работник", [
        validation.validation_chain(
            validation.data_required(),
            validation.number_range(min=1),
            validation.exists(Employee.model(), 'id'),
        ),
    ])


class CalendarUpdateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    start = field.date_time("Начало", [
        validation.not_required(allow_empty=False)
    ])

    end = field.date_time("Конец", [
        validation.not_required(allow_empty=False)
    ])
