import datetime
from index.base.repository import Base
from company.models import Worker


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

    worker = field.Foreign(
        Worker.model(),
        verbose_name="Работник",
        on_delete=rel.CASCADE,
    )  # type: Worker.model()

    def __str__(self):
        u = self.worker

        return "%s %s [%s]:(%s - %s)" % (
            u.first_name,
            u.last_name,
            self.start.date(),
            self.start.time(),
            self.end.time(),
        )

    class Meta:
        verbose_name = "Показатель работника"
        verbose_name_plural = "Показатели работника"
