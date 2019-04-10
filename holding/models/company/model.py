from app.base.model import Model as _Model


class Company(_Model):
    from django.db.models import fields as _field
    from app.fields import timezone as _timezone
    from django.db.models.fields import related as _related
    from django.db.models import deletion as _deletion

    name = _field.CharField(
        verbose_name="Название компании",
        max_length=200,
        null=False,
    )

    description = _field.TextField(
        verbose_name="Описание компании",
        max_length=4000,
        null=True,
        blank=True,
    )

    address = _field.CharField(
        verbose_name="Адрес компании",
        max_length=512,
        null=True,
        blank=True,
    )

    phone = _field.CharField(
        verbose_name="Телефон",
        max_length=32,
        null=True,
        blank=True,
    )

    email = _field.EmailField(
        verbose_name="Почтовый ящик",
        max_length=255,
        null=False,
    )

    from holding.models.employee.model import Employee as _Employee
    owner = _related.ForeignKey(
        _Employee,  # Changed company owner from user to employee because of the system flow
        verbose_name="Владелец",
        on_delete=_deletion.DO_NOTHING,
        null=False,
    )

    from pay.models.discount.model import Discount as _Discount
    discount = _related.ForeignKey(
        _Discount,
        on_delete=_deletion.SET_NULL,
        null=True,
        blank=True,
    )

    timezone = _timezone.TimeZoneField(
        "Локальное время компании",
        default="UTC",
        null=False,
        blank=True,
    )

    def __str__(self):
        return self.name

    @property
    def last_payment(self):
        from pay.models import Payment

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
