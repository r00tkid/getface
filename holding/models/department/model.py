from app.base.model import Model as _Model


class Department(_Model):
    from django.db.models import fields as _field
    from django.db.models.fields import related as _related
    from django.db.models import deletion as _deletion

    name = _field.CharField(
        verbose_name="Название отдела",
        max_length=255,
        null=False,
        blank=False,
    )

    from holding.models import Company as _Company
    company = _related.ForeignKey(
        _Company,
        on_delete=_deletion.CASCADE,
        null=False,
        blank=False,
        related_name="departments",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"
