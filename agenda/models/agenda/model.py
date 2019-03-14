from index.base.repository import Base
from employee.models.employee.model import Employee


class Agenda(Base.models.Model):
    relation = Base.models.Model.relation
    field = Base.models.Model.field

    start = field.date_time("Дата начала")
    end = field.date_time("Дата окончания")

    active = field.small_integer(
        "Активность",
        default=0,
    )

    mood = field.small_integer(
        "Настроение",
        default=0,
    )

    fatigue = field.small_integer(
        "Усталость",
        default=0,
    )

    employee = field.foreign(
        Employee,
        verbose_name="Сотрудник",
        on_delete=relation.cascade,
    )

    def __str__(self):
        from datetime import datetime

        employee: Employee = self.employee
        start: datetime = self.start
        end: datetime = self.end

        return "%s %s [%s]:(%s - %s)" % (
            employee.first_name,
            employee.last_name,

            start.date(),
            start.time(),
            end.time(),
        )

    class Meta:
        verbose_name = "Показатель сотрудника"
        verbose_name_plural = "Показатели сотрудников"
