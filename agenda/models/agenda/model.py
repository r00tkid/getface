import datetime
from index.base.repository import Base
from employee.models.employee.model import Employee


class Agenda(Base.TimeStumps, Base.SoftDeletion):
    field = Base.Model.field
    rel = Base.Model.rel

    start = field.DateTime("Дата начала")  # type: datetime.datetime
    end = field.DateTime("Дата окончания")  # type: datetime.datetime

    active = field.SmallInteger(
        "Активность",
        default=0,
    )

    mood = field.SmallInteger(
        "Настроение",
        default=0,
    )

    fatigue = field.SmallInteger(
        "Усталость",
        default=0,
    )

    employee = field.Foreign(
        Employee,
        verbose_name="Сотрудник",
        on_delete=rel.CASCADE,
    )

    def __str__(self):
        u: Employee = self.employee

        return "%s %s [%s]:(%s - %s)" % (
            u.first_name,
            u.last_name,
            self.start.date(),
            self.start.time(),
            self.end.time(),
        )

    class Meta:
        verbose_name = "Показатель сотрудника"
        verbose_name_plural = "Показатели сотрудников"
