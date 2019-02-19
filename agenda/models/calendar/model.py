import datetime
from index.base.repository import Base
from employee.models.employee.model import Employee


class Calendar(Base.TimeStumps, Base.SoftDeletion):
    field = Base.Model.field
    rel = Base.Model.rel

    start = field.DateTime("Дата начала")  # type: datetime.datetime
    end = field.DateTime("Дата окончания")  # type: datetime.datetime

    is_wanted = field.NullBoolean(
        "Хочет работать",
        default=None,
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
            self.end.time()
        )

    class Meta:
        verbose_name = "График сотрудника"
        verbose_name_plural = "Графики сотрудников"
