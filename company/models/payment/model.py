from index.base.repository import Base
from authentication.models import UserRepository
from company.models import CompanyRepository, RateRepository


class Payment(Base.TimeStumps, Base.SoftDeletion):
    field = Base.Model.field
    rel = Base.Model.rel

    # rate = field.Foreign(
    #     RateRepository.model(),
    #     on_delete=rel.CASCADE,
    #     null=False,
    # )

    info = field.Text(
        "Информация о платеже",
        null=False,
        blank=False,
        default="{}",
    )

    user = field.Foreign(
        UserRepository.model(),
        on_delete=rel.DO_NOTHING,
        verbose_name="Платильщик",
        null=True,
        blank=True,
    )

    company = field.Foreign(
        CompanyRepository.model(),
        on_delete=rel.DO_NOTHING,
        verbose_name="Компания",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"
