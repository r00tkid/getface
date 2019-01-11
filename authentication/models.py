from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(
        _('email address'),
        null=False,
        blank=False,
        unique=True,
    )

    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    def __str__(self):
        return "%s %s (%s)" % (self.first_name, self.last_name, self.username) if (
                self.first_name or self.last_name
        ) else (
                "%s" % self.username
        )

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
