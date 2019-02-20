from index.base.repository import Base
from company.models.company.model import Company


class Department(Base.TimeStumps, Base.SoftDeletion):
    field = Base.Model.field
    rel = Base.Model.rel

    name = field.Char(
        verbose_name="Название отдела/цеха",
        max_length=255,
        null=False,
        blank=False,
    )

    company = field.Foreign(
        Company,
        on_delete=rel.CASCADE,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"