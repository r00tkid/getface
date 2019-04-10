from app.base.model import Model as _Model


class PaymentDetails(_Model):
    from django.db.models.fields import related as _related
    from django.db.models import deletion as _deletion
    from django.db.models import fields as _field
    from datetime import datetime as _dt

    company = _related.ForeignKey(
        'holding.Company',
        on_delete=_deletion.CASCADE,
        null=False,
        blank=False,
    )

    rate = _related.ForeignKey(
        'pay.Rate',
        on_delete=_deletion.CASCADE,
        verbose_name="Выбранный тариф",
        null=False,
        blank=False,
    )

    discount = _related.ForeignKey(
        'pay.Discount',
        on_delete=_deletion.CASCADE,
        null=True,
        blank=False,
    )

    start = _field.DateTimeField(
        "Дата начала действия тарифа",
        default=_dt.now,
    )

    discount_percent = _field.PositiveSmallIntegerField(
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
