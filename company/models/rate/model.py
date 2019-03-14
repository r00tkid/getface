from index.base.repository import Base


class Rate(Base.models.Model):
    from datetime import timedelta

    field = Base.models.Model.field

    name = field.char(
        "Название",
        max_length=256,
        null=False,
        blank=False,
    )

    description = field.text(
        "Описание",
        null=False,
        blank=False,
    )

    per_month = field.float(
        "Цена за месяц",
        null=False,
        blank=False,
    )

    is_archived = field.boolean(
        "Архивный",
        null=False,
        default=False,
    )

    lifetime = field.duration(
        "Время действия тарифа",
        default=timedelta(days=30)
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"
