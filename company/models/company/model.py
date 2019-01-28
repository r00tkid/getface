from index.base.repository import Base
from authentication.models.user.model import User


class Company(Base.TimeStumps, Base.SoftDeletion):
    field = Base.Model.field
    rel = Base.Model.rel

    name = field.Char(
        verbose_name="Название компании",
        max_length=200,
        null=False,
    )

    description = field.Text(
        verbose_name="Описание компании",
        max_length=4000,
        null=True,
        blank=True,
    )

    address = field.Char(
        verbose_name="Адрес компании",
        max_length=512,
        null=True,
        blank=True,
    )

    phone = field.Char(
        verbose_name="Телефон",
        max_length=32,
        null=True,
        blank=True,
    )

    email = field.Char(
        verbose_name="Почтовый ящик",
        max_length=255,
        null=False,
    )

    owner = field.Foreign(
        User,
        verbose_name="Владелец",
        on_delete=rel.DO_NOTHING,
        null=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
