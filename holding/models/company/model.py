from app.base.model import Model as _Model
from django.db.models.fields import related as _related
from django.db.models import deletion as _deletion
from django.db.models import fields as _field


class CompanyCreator(_Model):
    creator = _related.OneToOneField(
        to='holding.Employee',
        on_delete=_deletion.DO_NOTHING,
        verbose_name='Создатель',
        related_name='creators',
    )

    company = _related.OneToOneField(
        to='holding.Company',
        on_delete=_deletion.CASCADE,
        verbose_name='Компания',
        related_name='companies',
    )

    physical = _related.OneToOneField(
        to='entry.User',
        on_delete=_deletion.DO_NOTHING,
        verbose_name='Физический пользователь',
        related_name='users',
        blank=True,
        null=True,
    )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.physical = self.creator.user

        super(CompanyCreator, self).save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = 'Основатель'
        verbose_name_plural = 'Основатели'


class Company(_Model):
    from app.fields import timezone as _timezone

    name = _field.CharField(
        verbose_name='Название компании',
        max_length=200,
        null=False,
    )

    description = _field.TextField(
        verbose_name='Описание компании',
        max_length=4000,
        null=True,
        blank=True,
    )

    address = _field.CharField(
        verbose_name='Адрес компании',
        max_length=512,
        null=True,
        blank=True,
    )

    phone = _field.CharField(
        verbose_name='Телефон',
        max_length=32,
        null=True,
        blank=True,
    )

    email = _field.EmailField(
        verbose_name='Почтовый ящик',
        max_length=255,
        null=False,
    )

    owner = _related.ForeignKey(
        'holding.Employee',  # Changed company owner from user to employee because of the system flow
        verbose_name='Владелец',
        on_delete=_deletion.DO_NOTHING,
        null=False,
        related_name='owner',
    )

    discount = _related.ForeignKey(
        to='pay.Discount',
        on_delete=_deletion.SET_NULL,
        null=True,
        blank=True,
    )

    timezone = _timezone.TimeZoneField(
        verbose_name='Локальное время компании',
        default='UTC',
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

    rate.fget.short_description = u'Тариф'

    @property
    def time_left(self):
        return self.last_payment.time_left if self.last_payment else -1

    time_left.fget.short_description = u"Оплаченное время"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        creation = True

        if self.id:
            creation = False

        super(Company, self).save(force_insert, force_update, using, update_fields)

        self.owner.company = self
        self.owner.save()

        if creation:
            CompanyCreator(creator=self.owner, company=self).save()

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
