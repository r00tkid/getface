from app.base.model import Model as _Model
from django.db.models import fields as _field
from app.fields import timezone as _timezone
from django.db.models.fields import related as _related
from django.db.models import deletion as _deletion


class Violation(_Model):
    employee = _related.ForeignKey(
        'holding.Employee',
        on_delete=_deletion.SET_NULL,
        null=True,
        blank=False,  # For admin panel?
        related_name="violations",
    )

    when = _field.DateTimeField("Когда")

    title = _field.CharField(
        verbose_name="Название нарушения",
        null=False,
        blank=False,
        max_length=128,
    )

    description = _field.TextField(
        verbose_name="Описание нарушения",
        null=True,
        blank=True,
    )

    timezone = _timezone.TimeZoneField(
        verbose_name="Временная зона",
        null=True,
        blank=True,
    )

    @property
    def employee_fullname(self):
        return "%s %s" % (self.employee.first_name, self.employee.last_name)

    employee_fullname.fget.short_description = "Сотрудник"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.timezone is None:
            self.timezone = self.employee.company.timezone

        return super(Violation, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Нарушение"
        verbose_name_plural = "Нарушения"
