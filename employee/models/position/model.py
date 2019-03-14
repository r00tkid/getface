from index.base.repository import Base
from company.models.company.model import Company


class Position(Base.models.Model):
    relation = Base.models.Model.relation
    field = Base.models.Model.field

    name = field.char(
        verbose_name="Название должности",
        max_length=255,
        null=False,
        blank=False,
    )

    company = field.foreign(
        Company,
        on_delete=relation.cascade,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
