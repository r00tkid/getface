# All imports here is for Django to see those models and for better use experience
from job.models.schedule import Schedule, ScheduleAdmin, ScheduleSerializer
from job.models.logbook import Logbook, LogbookAdmin, LogbookSerializer
from job.models.violation import Violation, ViolationAdmin, ViolationSerializer

# Getters
from app.base.helpers import get_model as __get


@__get(model=Schedule)
def get_schedule(id, raise_exception=True, obj=None) -> Schedule:
    return obj


@__get(model=Logbook)
def get_logbook(id, raise_exception=True, obj=None) -> Logbook:
    return obj


@__get(model=Violation)
def get_violation(id, raise_exception=True, obj=None) -> Violation:
    return obj
