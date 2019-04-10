from app.base.model import Model as _Model


class Payment(_Model):
    from django.db.models import fields as _field
    from django.db.models.fields import related as _related
    from django.db.models import deletion as _deletion

    from entry.models.user.model import User as _User
    user = _related.ForeignKey(
        _User,
        on_delete=_deletion.DO_NOTHING,
        verbose_name="Платильщик",
        null=True,
        blank=True,
    )

    from pay.models.discount.model import Discount as _Discount
    discount = _related.ForeignKey(
        _Discount,
        on_delete=_deletion.SET_NULL,
        null=True,
        blank=True,
    )

    info = _field.TextField(
        "Информация о платеже",
        null=False,
        blank=False,
        default="{}",
    )

    from pay.models.detail.model import PaymentDetails as _Details
    details = _related.OneToOneField(
        _Details,
        on_delete=_deletion.PROTECT,
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
