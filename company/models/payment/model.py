from index.base.repository import Base
from authentication.models import User
from company.models import Company, Rate


class Payment(Base.TimeStumps, Base.SoftDeletion):
    field = Base.Model.field
    rel = Base.Model.rel

    rate = field.Foreign(
        Rate.model(),
        on_delete=rel.CASCADE,
        null=False,
    )

    info = field.Text(
        "Информация о платеже",
        null=False,
        blank=False,
        default="{}",
    )

    user = field.Foreign(
        User.model(),
        on_delete=rel.DO_NOTHING,
        verbose_name="Платильщик",
        null=True,
        blank=True,
    )

    company = field.Foreign(
        Company.model(),
        on_delete=rel.DO_NOTHING,
        verbose_name="Компания",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"
