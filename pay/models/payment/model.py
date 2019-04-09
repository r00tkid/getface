from app.base.model import Model as _Model
from django.db.models import fields as _field
from app.fields import timezone as _timezone
from django.db.models.fields import related as _related
from django.db.models import deletion as _deletion


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
