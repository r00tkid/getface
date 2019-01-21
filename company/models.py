__all__ = ('Company', 'Worker')

from authentication.models.user.model import get_user_model
from index.base.abstract import SoftDeletesModel, models
import uuid

User = get_user_model()


class Company(SoftDeletesModel):
    name = models.CharField(
        verbose_name="Название компании",
        max_length=200,
        null=False,
    )

    description = models.TextField(
        verbose_name="Описание компании",
        max_length=4000,
        null=True,
        blank=True,
    )

    address = models.CharField(
        verbose_name="Адрес компании",
        max_length=512,
        null=True,
        blank=True,
    )

    phone = models.CharField(
        verbose_name="Телефон",
        max_length=32,
        null=True,
        blank=True,
    )

    email = models.CharField(
        verbose_name="Почтовый ящик",
        max_length=255,
        null=False,
    )

    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        on_delete=models.DO_NOTHING,
        null=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


class Worker(SoftDeletesModel):
    first_name = models.CharField(
        max_length=200,
        verbose_name="Имя",
    )

    last_name = models.CharField(
        max_length=200,
        verbose_name="Фамилия",
    )

    phone = models.CharField(
        max_length=200,
        verbose_name="Телефон",
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Физический пользователь",
        null=True,
        blank=True,
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name="Компания",
        null=False,
        blank=False,
    )

    is_manager = models.BooleanField(
        verbose_name="Менеджер",
        default=False,
    )

    is_fired = models.BooleanField(
        verbose_name="Уволен",
        default=False,
    )

    auth_key = models.UUIDField(
        verbose_name="Уникальный авторизационный ключ",
        editable=False,
        unique=True,
        null=True,
        blank=False,
        default=uuid.uuid4,
    )

    email = models.CharField(
        max_length=256,
        verbose_name="E-mail",
        null=True,
        blank=True,
    )

    def __str__(self):
        return "%s %s" % (self.last_name, self.first_name) + (
            " (" + self.user.username + ")" if self.user_id else ""
        )

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"
        unique_together = (('user', 'company'),)


class Rate(SoftDeletesModel):
    name = models.CharField(
        "Название",
        max_length=256,
        null=False,
        blank=False,
    )

    description = models.TextField(
        "Описание",
        null=False,
        blank=False,
    )

    per_month = models.FloatField(
        "Цена за месяц (руб)",
        null=False,
        blank=False,
    )

    is_archived = models.BooleanField(
        "Архивный",
        null=False,
        default=False,
    )

    class Meta:
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"


class Payment(SoftDeletesModel):
    rate = models.ForeignKey(
        Rate,
        on_delete=models.CASCADE,
        null=False,
    )

    info = models.TextField(
        "Информация о платеже",
        null=False,
        blank=False,
        default="{}",
    )

    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name="Платильщик",
        null=True,
        blank=True,
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.DO_NOTHING,
        verbose_name="Компания",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"
