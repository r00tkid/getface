from app.base.model import Model as _Model


class Schedule(_Model):
    from django.db.models.fields import related as _related
    from django.db.models import deletion as _deletion
    from django.db.models import fields as _field
    from app.fields import timezone as _timezone

    employee = _related.ForeignKey(
        'holding.Employee',
        on_delete=_deletion.SET_NULL,
        null=True,
        blank=False,  # For admin panel?
        related_name="schedules",
    )

    start = _field.DateTimeField("Начало")
    end = _field.DateTimeField("Конец")

    is_wanted = _field.NullBooleanField(
        verbose_name="Хочет работать",
        default=None,
    )

    timezone = _timezone.TimeZoneField(
        verbose_name="Временная зона",
        null=True,
        blank=True,
    )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.timezone is None:
            self.timezone = self.company.timezone

        return super(Schedule, self).save(force_insert, force_update, using, update_fields)

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
            self.end.time()
        )

    class Meta:
        verbose_name = "График сотрудника"
        verbose_name_plural = "Графики сотрудников"
