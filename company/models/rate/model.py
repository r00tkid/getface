from index.base.repository import Base


class Rate(Base.TimeStumps, Base.SoftDeletion):
    field = Base.Model.field

    name = field.Char(
        "Название",
        max_length=256,
        null=False,
        blank=False,
    )

    description = field.Text(
        "Описание",
        null=False,
        blank=False,
    )

    per_month = field.Float(
        "Цена за месяц (руб)",
        null=False,
        blank=False,
    )

    is_archived = field.Boolean(
        "Архивный",
        null=False,
        default=False,
    )

    class Meta:
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"
