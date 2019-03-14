from index.base.repository import Base


class Payment(Base.models.Model):
    from authentication.models.user.model import User as __User
    from company.models.discount.model import Discount as __Discount

    __rate_to_company = None

    relation = Base.models.Model.relation
    field = Base.models.Model.field

    user = field.foreign(
        __User,
        on_delete=relation.do_nothing,
        verbose_name="Платильщик",
        null=True,
        blank=True,
    )

    discount = field.foreign(
        __Discount,
        on_delete=relation.set_null,
        null=True,
        blank=True,
    )

    info = field.text(
        "Информация о платеже",
        null=False,
        blank=False,
        default="{}",
    )

    def __init_rate_to_company(self):
        from company.models.payment.model import PaymentDetails

        if not self.__rate_to_company:
            self.__rate_to_company: PaymentDetails = PaymentDetails.all.filter(payment=self).first()

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

    rate_to_company.fget.short_description = u"Текущий тариф"

    @property
    def time_left(self):
        from datetime import datetime

        rtc = self.__init_rate_to_company()

        if rtc and self.rate:
            return rtc.start + self.rate.lifetime - datetime.now()

        return -0

    time_left.fget.short_description = u"Остаток времени по текущему тарифу"

    def __str__(self):
        return "Оплата от пользователя [%s] за компанию [%s] по тарифу [%s]." % (str(self.user), str(self.company), str(self.rate))

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"


class PaymentDetails(Base.models.Model):
    from company.models.discount.model import Discount as __Discount
    from company.models.company.model import Company as __Company
    from company.models.rate.model import Rate as __Rate
    from datetime import datetime

    relation = Base.models.Model.relation
    field = Base.models.Model.field

    # Main relation
    payment = field.one_to_one(
        Payment,
        on_delete=relation.cascade,
        null=False,
        blank=False,
    )

    company = field.foreign(
        __Company,
        on_delete=relation.cascade,
        null=False,
        blank=False,
    )

    rate = field.foreign(
        __Rate,
        on_delete=relation.cascade,
        verbose_name="Выбранный тариф",
        null=False,
        blank=False,
    )

    discount = field.foreign(
        __Discount,
        on_delete=relation.set_null,
        null=True,
        blank=False,
    )

    start = field.date_time(
        "Дата начала действия тарифа",
        default=datetime.now
    )

    discount_percent = field.float(
        "Процент скидки на момент платежа",
        default=None,
        null=True,
        blank=True,
    )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.discount:
            self.discount = self.company.discount

        if self.discount:
            self.discount_percent = self.discount.percent

        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
