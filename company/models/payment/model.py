from index.base.repository import Base


class PaymentDetails(Base.models.Model):
    from company.models.discount.model import Discount as __Discount
    from company.models.company.model import Company as __Company
    from company.models.rate.model import Rate as __Rate
    from datetime import datetime

    relation = Base.models.Model.relation
    field = Base.models.Model.field

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

    class Meta:
        verbose_name = "Дополнительные детали"
        verbose_name_plural = "Детали оплат"


class Payment(Base.models.Model):
    from authentication.models.user.model import User as __User
    from company.models.discount.model import Discount as __Discount

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

    details = field.one_to_one(
        PaymentDetails,
        on_delete=relation.protect,
        verbose_name="Детали",
        related_name="payment",
    )

    @property
    def company(self):
        return self.details.company if self.details else None

    @property
    def rate(self):
        return self.details.rate if self.details else None

    @property
    def time_left(self):
        from datetime import datetime

        if self.details and self.rate:
            # Cast details start to native datetime
            return self.details.start.replace(tzinfo=None) + self.rate.lifetime - datetime.now()

        return -0

    time_left.fget.short_description = u"Остаток времени по текущему тарифу"

    def __str__(self):
        return "Оплата от пользователя [%s] за компанию [%s] по тарифу [%s]." % (str(self.user), str(self.company), str(self.rate))

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"
