from app.base.model import Model as _Model


class Discount(_Model):
    from django.db.models import fields as _field

    name = _field.CharField(
        verbose_name="Название скидки",
        max_length=200,
        null=False,
        blank=False,
    )

    percent = _field.PositiveSmallIntegerField(
        verbose_name="Процент",
        default=0,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"
