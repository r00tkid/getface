from index.base.repository import Base
from company.models.company.model import Company


class WorkerDepartment(Base.TimeStumps, Base.SoftDeletion):
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

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"
