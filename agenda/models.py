import datetime
from app.base import abstract

models = abstract.models


class WorkerAgenda(abstract.SoftDeletesModel):
    start = models.DateTimeField("Дата начала")
    end = models.DateTimeField("Дата окончания")


class DailyAgenda(abstract.SoftDeletesModel):
    start = models.DateTimeField("Дата начала")
    end = models.DateTimeField("Дата окончания")
