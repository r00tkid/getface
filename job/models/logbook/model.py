from app.base.model import Model as _Model


class Logbook(_Model):
    from django.db.models.fields import related as _related
    from django.db.models import deletion as _deletion
    from django.db.models import fields as _field
    from app.fields import timezone as _timezone

    employee = _related.ForeignKey(
        'holding.Employee',
        on_delete=_deletion.SET_NULL,
        null=True,
        blank=False,  # For admin panel?
        related_name="logbooks",
    )

    start = _field.DateTimeField("Начало отрезка")
    end = _field.DateTimeField("Конец отрезка")

    activity = _field.PositiveSmallIntegerField(
        verbose_name="Активность",
        default=0,
    )

    mood = _field.PositiveSmallIntegerField(
        verbose_name="Настроение",
        default=0,
    )

    fatigue = _field.PositiveSmallIntegerField(
        verbose_name="Усталость",
        default=0,
    )

    timezone = _timezone.TimeZoneField(
        verbose_name="Временная зона",
        null=True,
        blank=True,
    )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.timezone is None:
            self.timezone = self.company.timezone

        return super(Logbook, self).save(force_insert, force_update, using, update_fields)

    @property
    def employee_fullname(self):
        return "%s %s" % (self.employee.first_name, self.employee.last_name)

    employee_fullname.fget.short_description = "Сотрудник"

    @property
    def company(self):
        return self.employee.company

    company.fget.short_description = "Компания"

    @property
    def company_name(self):
        return self.company.name

    company_name.fget.short_description = "Компания"

    def __str__(self):
        return "%s %s [%s]:(%s - %s)" % (
            self.employee.first_name,
            self.employee.last_name,

            self.start.date(),
            self.start.time(),
            self.end.time(),
        )

    class Meta:
        verbose_name = "Показатель сотрудника"
        verbose_name_plural = "Показатели сотрудников"
