from index.base.repository import Base
from employee.models.employee.model import Employee


class Calendar(Base.models.Model):
    relations = Base.models.Model.relations
    field = Base.models.Model.field

    start = field.DateTime("Дата начала")
    end = field.DateTime("Дата окончания")

    is_wanted = field.NullBoolean(
        "Хочет работать",
        default=None,
    )

    employee = field.Foreign(
        Employee,
        verbose_name="Сотрудник",
        on_delete=relations.CASCADE,
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
            end.time()
        )

    class Meta:
        verbose_name = "График сотрудника"
        verbose_name_plural = "Графики сотрудников"
