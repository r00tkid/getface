from app.base.model import Model as _Model
from django.db.models import fields as _field
from django.db.models.fields import related as _related
from django.db.models import deletion as _deletion


class Position(_Model):
    name = _field.CharField(
        verbose_name="Название должности",
        max_length=255,
        null=False,
        blank=False,
    )

    company = _related.ForeignKey(
        'holding.Company',
        on_delete=_deletion.SET_NULL,
        null=True,
        blank=True,
        related_name="positions",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"


class PositionToDepartment(_Model):
    position = _related.ForeignKey(
        Position,
        on_delete=_deletion.CASCADE,
        null=False,
        blank=False,
    )

    from holding.models import Department as _Department
    department = _related.ForeignKey(
        _Department,
        on_delete=_deletion.CASCADE,
        null=False,
        blank=False,
        related_name="positions",
    )

    def __str__(self):
        return "Должность %s из отдела %s (%s)" % (self.position, self.department, self.position.company)

    class Meta:
        verbose_name = "Должность к отделу"
        verbose_name_plural = "Должности к отделу"
