from index.base.repository import Base
from company.models import Worker


class Calendar(Base.TimeStumps, Base.SoftDeletion):
    field = Base.Model.field
    rel = Base.Model.rel

    start = field.DateTime("Дата начала")
    end = field.DateTime("Дата окончания")

    is_wanted = field.NullBoolean(
        "Хочет работать",
        default=None,
    )

    worker = field.Foreign(
        Worker.model(),
        verbose_name="Работник",
        on_delete=rel.CASCADE,
    )

    def __str__(self):
        u = self.worker

        return "%s %s [%s]:(%s - %s)" % (
            u.first_name,
            u.last_name,
            self.start.date(),
            self.start.time(),
            self.end.time()
        )

    class Meta:
        verbose_name = "График работника"
        verbose_name_plural = "Графики работника"
