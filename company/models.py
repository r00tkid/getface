from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(
        null=False,
        max_length=200,
        verbose_name="Название компании"
    )


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
        null=False,
        blank=False,
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
        default=0,
    )

    def email(self):
        return self.user.email
