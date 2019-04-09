from app.base.model import Model as _Model
from django.db.models import fields as _field
from app.fields import timezone as _timezone
from django.db.models.fields import related as _related
from django.db.models import deletion as _deletion


class Discount(Base.models.Model):
    field = Base.models.Model.field

    name = field.char(
        verbose_name="Название скидки",
        max_length=200,
        null=False,
        blank=False,
    )

    percent = field.small_integer(
        verbose_name="Процент",
        default=0,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"
