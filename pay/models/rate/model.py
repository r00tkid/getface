from app.base.model import Model as _Model


class Rate(_Model):
    from django.db.models import fields as _field
    from datetime import timedelta as _td

    name = _field.CharField(
        "Название",
        max_length=256,
        null=False,
        blank=False,
    )

    description = _field.CharField(
        "Описание",
        null=False,
        blank=False,
    )

    per_month = _field.FloatField(
        "Цена за месяц",
        null=False,
        blank=False,
    )

    is_archived = _field.BooleanField(
        "Архивный",
        null=False,
        default=False,
    )

    lifetime = _field.DurationField(
        "Время действия тарифа",
        default=_td(days=30),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"
