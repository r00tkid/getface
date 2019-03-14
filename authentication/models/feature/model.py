from index.base.repository import Base


class Feature(Base.models.Model):
    field = Base.models.Model.field

    name = field.char(
        "Название",
        max_length=256,
        null=False,
        blank=False,
    )

    link = field.char(
        "Ссылка",
        max_length=1024,
        null=True,
        blank=True,
    )

    description = field.text(
        "Описание",
        max_length=5000,
        null=False,
        blank=False,
    )

    is_alive = field.boolean(
        "Существует",
        default=True,
    )

    is_important = field.boolean(
        "Важная",
        default=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фича'
        verbose_name_plural = 'Фичи'
