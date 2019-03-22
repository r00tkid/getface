from index.base.repository import Base
from authentication.models.user.model import User
from company.models.rate.model import Rate
from company.models.discount.model import Discount


class Company(Base.models.Model):
    relation = Base.models.Model.relation
    field = Base.models.Model.field

    name = field.char(
        verbose_name="Название компании",
        max_length=200,
        null=False,
    )

    description = field.text(
        verbose_name="Описание компании",
        max_length=4000,
        null=True,
        blank=True,
    )

    address = field.char(
        verbose_name="Адрес компании",
        max_length=512,
        null=True,
        blank=True,
    )

    phone = field.char(
        verbose_name="Телефон",
        max_length=32,
        null=True,
        blank=True,
    )

    email = field.email(
        verbose_name="Почтовый ящик",
        max_length=255,
        null=False,
    )

    owner = field.foreign(
        User,
        verbose_name="Владелец",
        on_delete=relation.do_nothing,
        null=False,
    )

    discount = field.foreign(
        Discount,
        on_delete=relation.set_null,
        null=True,
        blank=True,
    )

    timezone = field.time_zone(
        "Локальное время компании",
        default="UTC",
        null=False,
        blank=True,
    )

    def __str__(self):
        return self.name

    @property
    def last_payment(self):
        from company.models.payment.model import Payment

        return Payment.objects.filter(details__company=self).last()

    @property
    def rate(self):
        return self.last_payment.details.rate if self.last_payment else None

    @property
    def time_left(self):
        return self.last_payment.time_left if self.last_payment else -1

    time_left.fget.short_description = u"Оплаченное время"

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
