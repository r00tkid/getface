from app.base.model import Model as _Model


class Face(_Model):
    from django.contrib.contenttypes.fields import GenericRelation as _Generic
    from django.db.models.fields import related as _related
    from django.db.models import deletion as _deletion
    from django.db.models import fields as _field

    employee = _related.ForeignKey(
        'holding.Employee',
        on_delete=_deletion.CASCADE,
        null=False,
        blank=False,
    )

    face_id = _field.CharField(
        verbose_name="Face ID",
        max_length=64,
    )

    photo = _Generic(
        'common.Image',
        verbose_name="Фотография",
        null=True,
    )

    class Meta:
        verbose_name = "Лицо"
        verbose_name_plural = "Лица"
