from index.base.repository import Base
from authentication.models.user.model import User
from company.models.company.model import Company
from company.models.rate.model import Rate
from company.models.discount.model import Discount


class Payment(Base.TimeStumps, Base.SoftDeletion):
    field = Base.Model.field
    rel = Base.Model.rel

    user = field.Foreign(
        User,
        on_delete=rel.DO_NOTHING,
        verbose_name="Платильщик",
        null=True,
        blank=True,
    )

    rate = field.Foreign(
        Rate,
        on_delete=rel.CASCADE,
        null=False,
    )

    discount = field.Foreign(
        Discount,
        on_delete=rel.SET(None),
        null=True,
        blank=True,
    )

    info = field.Text(
        "Информация о платеже",
        null=False,
        blank=False,
        default="{}",
    )

    company = field.Foreign(
        Company,
        on_delete=rel.DO_NOTHING,
        verbose_name="Компания",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"
