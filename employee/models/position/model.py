from index.base.repository import Base
from company.models.company.model import Company


class Position(Base.models.Model):
    relations = Base.models.Model.relations
    field = Base.models.Model.field

    name = field.Char(
        verbose_name="Название должности",
        max_length=255,
        null=False,
        blank=False,
    )

    company = field.Foreign(
        Company,
        on_delete=relations.CASCADE,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
