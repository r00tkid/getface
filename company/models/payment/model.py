from index.base.repository import Base


class Payment(Base.models.Model):
    from authentication.models.user.model import User as __User
    from company.models.discount.model import Discount as __Discount
    from company.models.rate.model import RateToCompany as __RateToCompany

    __rate_to_company = None

    relations = Base.models.Model.relations
    field = Base.models.Model.field

    user = field.Foreign(
        __User,
        on_delete=relations.DO_NOTHING,
        verbose_name="Платильщик",
        null=True,
        blank=True,
    )

    discount = field.Foreign(
        __Discount,
        on_delete=relations.SET(None),
        null=True,
        blank=True,
    )

    discount_percent = field.Float(
        "Процент скидки на момент платежа",
        default=None,
        null=True,
        blank=True,
    )

    info = field.Text(
        "Информация о платеже",
        null=False,
        blank=False,
        default="{}",
    )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.discount:
            self.discount_percent = self.discount.percent

        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def __init_rate_to_company(self) -> __RateToCompany:
        if not self.__rate_to_company:
            self.__rate_to_company = Payment.__RateToCompany.all.filter(payment=self).first()

        return self.__rate_to_company

    @property
    def company(self):
        rtc = self.__init_rate_to_company()

        return rtc.company if rtc else None

    @property
    def rate(self):
        rtc = self.__init_rate_to_company()

        return rtc.rate if rtc else None

    @property
    def rate_to_company(self):
        return self.__init_rate_to_company()

    rate_to_company.verbose_name = "Текущий тариф"

    @property
    def time_left(self):
        from datetime import datetime

        rtc = self.__init_rate_to_company()

        if rtc and self.rate:
            return rtc.start + self.rate.lifetime - datetime.now()

        return -0

    time_left.verbose_name = "Остаток времени по текущему тарифу"

    def __str__(self):
        return "Оплата от пользователя [%s] за компанию [%s] по тарифу [%s]." % (str(self.user), str(self.company), str(self.rate))

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"


class PaymentCompanyRateDiscount():
    pass
