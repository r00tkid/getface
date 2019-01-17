__all__ = ('get_user_model', 'User')

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model as default_user
from app.base.abstract import Model, SoftDeletesModel


class User(AbstractUser):
    email = models.EmailField(
        _('email address'),
        null=False,
        blank=False,
        unique=True,
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,  # Causes problems with super users if is not set to True. Handle base user active in views.
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    phone = models.CharField(
        "Телефон",
        max_length=30,
        null=False,
        blank=False,
    )

    def __str__(self):
        return "%s %s (%s)" % (self.first_name, self.last_name, self.username) if (
                self.first_name or self.last_name
        ) else (
                "%s" % self.username
        )

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Feature(SoftDeletesModel):
    name = models.CharField(
        "Название",
        max_length=512,
        null=False,
        blank=False,
    )

    link = models.CharField(
        "Ссылка",
        max_length=1024,
        null=False,
        blank=False,
    )

    description = models.TextField(
        "Описание",
        null=False,
        blank=False,
    )

    is_alive = models.BooleanField(
        "Существует",
        default=True,
    )

    is_important = models.BooleanField(
        "Важная",
        default=False,
    )

    class Meta:
        verbose_name = 'Фича'
        verbose_name_plural = 'Фичи'


class Progress(Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        null=False,
        blank=False,
    )

    feature = models.ForeignKey(
        Feature,
        on_delete=models.CASCADE,
        verbose_name="Фича",
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = 'Прогресс'
        verbose_name_plural = 'Прогресс'


def get_user_model():
    return default_user() if default_user() else User
