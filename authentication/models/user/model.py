from django.contrib.auth.models import AbstractUser
from index.base.repository import Base


class User(AbstractUser, Base.CreatedStump):
    field = Base.Model.field

    email = field.Email(
        "E-mail",
        null=False,
        blank=False,
        unique=True,
    )

    is_active = field.Boolean(
        "Актив",
        default=True,  # Causes problems with super users if is not set to True. Handle base user active in views.
    )

    phone = field.Char(
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
