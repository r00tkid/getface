from django.contrib.auth.models import AbstractUser as _Abstract
from app.base.model import Model as _Model
from app.mail import Sandman as _Mail
import os as _os


def _activation_key() -> str:
    import _md5
    import uuid

    return _md5.md5(uuid.uuid4().bytes).hexdigest()


class User(_Abstract, _Model):
    from django.db.models import fields as _field
    from app.fields import timezone as _timezone

    email = _field.EmailField(
        verbose_name='E-mail',
        null=False,
        blank=False,
        unique=True,
        max_length=256,
    )

    phone = _field.CharField(
        verbose_name='Телефон',
        max_length=30,
        null=False,
        blank=False,
    )

    activation = _field.CharField(
        verbose_name='Код активации/восстановления пароля',
        max_length=255,
        null=True,
        editable=False,
        default=_activation_key
    )

    timezone = _timezone.TimeZoneField(
        verbose_name='Локальное время пользователя',
        default='UTC',
        null=False,
        blank=True,
    )

    is_active = _field.BooleanField(
        verbose_name='Активирован',
        default=True,  # Causes problems with super users if is not set to True. Handle base user active in views.
    )

    is_banned = _field.BooleanField(
        verbose_name='Забанен',
        default=False,
    )

    def new_activation(self):
        self.activation = _activation_key()
        return self.activation

    def check_activation(self, code):
        if self.activation is None or code is None or code == '':
            return False

        return self.activation == code

    def activate(self):
        """ Modificates user activation and save """
        self.is_active = True
        self.activation = None
        self.save()

    def deactivate(self):
        """ Modificates user activation and save """
        self.is_active = False
        self.activation = None
        self.save()

    def get_token(self):
        from entry.jwt import create_token
        return create_token(self)

    def __str__(self):
        return "%s %s (%s)" % (self.first_name, self.last_name, self.username) if (
                self.first_name or self.last_name
        ) else (
                "%s" % self.username
        )

    def reactivate(self):
        self.new_activation()
        self.save()

    # Mails part
    def mail_default(self, subject, template):
        from django.conf import settings

        _Mail(
            mail_from=settings.EMAIL_ADDRESSES.get('main'),
            mail_to=self.email,
            subject=subject,
            template=template,
            context={
                'user': self,
            }
        ).start()

    def mail_activation(self):
        self.mail_default(
            template='user%sregister' % _os.sep,
            subject="Registration",
        )

    def mail_activation_resend(self):
        self.reactivate()

        self.mail_default(
            template='user%sregister' % _os.sep,
            subject="Repeat registration mail",
        )

    def mail_reset_password(self):
        self.reactivate()

        self.mail_default(
            template='user%snew_password' % _os.sep,
            subject="Password restoration",
        )

    class Meta(_Abstract.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
