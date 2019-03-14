import _md5
import uuid
from django.contrib.auth.models import AbstractUser
from index.base.repository import Base


def _activation_key() -> str:
    return _md5.md5(uuid.uuid4().bytes).hexdigest()


class User(AbstractUser, Base.models.Model):
    field = Base.models.Model.field

    email = field.email(
        "E-mail",
        null=False,
        blank=False,
        unique=True,
    )

    is_active = field.boolean(
        "Актив",
        default=True,  # Causes problems with super users if is not set to True. Handle base user active in views.
    )

    phone = field.char(
        "Телефон",
        max_length=30,
        null=False,
        blank=False,
    )

    activation = field.char(
        verbose_name="Код активации/восстановления пароля",
        max_length=255,
        null=True,
        editable=False,
        default=_activation_key
    )

    timezone = field.time_zone(
        verbose_name="Локальное время пользователя",
        default="UTC",
        null=False,
        blank=True,
    )

    def new_activation(self):
        self.activation = _activation_key()
        return self.activation

    def check_activation(self, code):
        if self.activation is None or code is None or code == '':
            return False

        return self.activation == code

    def get_token(self):
        from authentication.jwt import create_token
        return create_token(self)

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
