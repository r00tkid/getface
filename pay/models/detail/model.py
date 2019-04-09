from app.base.model import Model as _Model
from django.db.models import fields as _field
from app.fields import timezone as _timezone
from django.db.models.fields import related as _related
from django.db.models import deletion as _deletion


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
