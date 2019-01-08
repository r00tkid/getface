from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(
        verbose_name="Название компании",
        max_length=200,
        null=False,
    )

    address = models.CharField(
        verbose_name="Адрес компании",
        max_length=512,
        null=False,
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
        null=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


# Create your models here.
class Worker(models.Model):
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

    def email(self):
        return self.user.email if self.user_id else ""

    def __str__(self):
        return "%s %s" % (self.last_name, self.first_name) + (
            " (" + self.user.username + ")" if self.user_id else ""
        )

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"
