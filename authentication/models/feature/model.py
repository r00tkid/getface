from index.base.repository import Base


class Feature(Base.TimeStumps, Base.SoftDeletion):
    field = Base.Model.field

    name = field.Char(
        "Название",
        max_length=256,
        null=False,
        blank=False,
    )

    link = field.Char(
        "Ссылка",
        max_length=1024,
        null=True,
        blank=True,
    )

    description = field.Text(
        "Описание",
        max_length=5000,
        null=False,
        blank=False,
    )

    is_alive = field.Boolean(
        "Существует",
        default=True,
    )

    is_important = field.Boolean(
        "Важная",
        default=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фича'
        verbose_name_plural = 'Фичи'
