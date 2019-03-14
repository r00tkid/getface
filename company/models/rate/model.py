from index.base.repository import Base


class Rate(Base.models.Model):
    from datetime import timedelta

    field = Base.models.Model.field

    name = field.Char(
        "Название",
        max_length=256,
        null=False,
        blank=False,
    )

    description = field.Text(
        "Описание",
        null=False,
        blank=False,
    )

    per_month = field.Float(
        "Цена за месяц",
        null=False,
        blank=False,
    )

    is_archived = field.Boolean(
        "Архивный",
        null=False,
        default=False,
    )

    lifetime = field.Duration(
        "Время действия тарифа",
        default=timedelta(days=30)
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"


class RateToCompany(Base.models.Model):
    from company.models.company.model import Company as __Company
    from company.models.payment.model import Payment as __Payment
    from datetime import datetime

    relations = Base.models.Model.relations
    field = Base.models.Model.field

    rate = field.Foreign(
        Rate,
        on_delete=relations.CASCADE,
        verbose_name="Актуальный тариф",
        null=False,
        blank=False,
    )

    company = field.Foreign(
        __Company,
        on_delete=relations.CASCADE,
        null=False,
        blank=False,
    )

    payment = field.OneToOne(
        __Payment,
        on_delete=relations.CASCADE,
        null=False,
        blank=False,
    )

    start = field.DateTime(
        "Дата начала действия тарифа",
        default=datetime.now()
    )
