import uuid
from index.base.repository import Base
from authentication.models.user.model import User
from company.models.company.model import Company


class Worker(Base.TimeStumps, Base.SoftDeletion):
    field = Base.Model.field
    rel = Base.Model.rel

    first_name = field.Char(
        max_length=200,
        verbose_name="Имя",
    )

    last_name = field.Char(
        max_length=200,
        verbose_name="Фамилия",
    )

    phone = field.Char(
        max_length=200,
        verbose_name="Телефон",
        null=True,
        blank=True,
    )

    user = field.Foreign(
        User,
        on_delete=rel.CASCADE,
        verbose_name="Физический пользователь",
        null=True,
        blank=True,
    )

    company = field.Foreign(
        Company,
        on_delete=rel.CASCADE,
        verbose_name="Компания",
        null=False,
        blank=False,
    )

    is_manager = field.Boolean(
        verbose_name="Менеджер",
        default=False,
    )

    is_fired = field.Boolean(
        verbose_name="Уволен",
        default=False,
    )

    auth_key = field.UUID(
        verbose_name="Уникальный авторизационный ключ",
        editable=False,
        unique=True,
        null=True,
        blank=False,
        default=uuid.uuid4,
    )

    email = field.Char(
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
