import datetime
from app.base import abstract
from company.models import Worker

models = abstract.models


class WorkerAgenda(abstract.SoftDeletesModel):
    start = models.DateTimeField("Дата начала")
    end = models.DateTimeField("Дата окончания")

    is_wanted = models.BooleanField(
        "Хочет работать",
        null=True,
        blank=True,
        default=None,
    )

    worker = models.ForeignKey(
        Worker,
        verbose_name="Работник",
        on_delete=models.CASCADE,
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


class WorkerFaceTime(abstract.SoftDeletesModel):
    start = models.DateTimeField("Дата начала")
    end = models.DateTimeField("Дата окончания")

    active = models.IntegerField(
        "Активность",
        default=0,
    )

    mood = models.IntegerField(
        "Настроение",
        default=0,
    )

    worker = models.ForeignKey(
        Worker,
        verbose_name="Работник",
        on_delete=models.CASCADE,
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
        verbose_name = "Показатель работника"
        verbose_name_plural = "Показатели работника"
