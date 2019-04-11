from app.base.model import Model as _Model


class Zone(_Model):
    from django.db.models.fields import related as _related
    from django.db.models import deletion as _deletion
    from django.db.models import fields as _field

    company = _related.ForeignKey(
        'holding.Company',
        on_delete=_deletion.CASCADE,
        related_name="zones",
    )

    name = _field.CharField(
        verbose_name="Название",
        max_length=128,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Зона"
        verbose_name_plural = "Зоны"
