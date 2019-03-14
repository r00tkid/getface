from index.base.repository import Base


class Discount(Base.models.Model):
    relations = Base.models.Model.relations
    field = Base.models.Model.field

    name = field.Char(
        verbose_name="Название скидки",
        max_length=200,
        null=False,
        blank=False,
    )

    percent = field.SmallInteger(
        verbose_name="Процент",
        default=0,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"
