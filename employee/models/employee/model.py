import uuid
from datetime import datetime
from index.base.repository import Base
from authentication.models.user.model import User
from company.models.company.model import Company

from employee.models.position.model import Position
from employee.models.department.model import Department


class Employee(Base.models.Model):
    relations = Base.models.Model.relations
    field = Base.models.Model.field

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

    company = field.Foreign(
        Company,
        on_delete=relations.CASCADE,
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

    email = field.Email(
        verbose_name="E-mail",
        null=True,
        blank=True,
    )

    timezone = field.TimeZone(
        verbose_name="Локальное время работника",
        default="UTC",
        null=False,
        blank=True,
    )

    invitation = field.DateTime(
        verbose_name="Последнее приглашение",
        null=True,
        blank=True,
    )

    is_invited = field.Boolean(
        verbose_name="Приглашён",
        null=False,
        default=False,
    )

    is_active = field.Boolean(
        verbose_name="Активен",
        null=False,
        default=False,
    )

    face_id = field.UUID(
        verbose_name="Face ID",
        null=True,
        blank=True,
    )

    user = field.Foreign(
        User,
        on_delete=relations.CASCADE,
        verbose_name="Физический пользователь",
        null=True,
        blank=True,
    )

    department = field.Foreign(
        Department,
        on_delete=relations.SET(None),
        default=None,
        null=True,
        blank=True,
    )

    position = field.Foreign(
        Position,
        on_delete=relations.SET(None),
        default=None,
        null=True,
        blank=True,
    )

    def clear_face_id(self):
        self.face_id = None

    def new_face_id(self):
        self.face_id = uuid.uuid4()

    def new_invitation(self):
        old = self.invitation
        self.invitation = datetime.now()
        return old

    def __str__(self):
        user: User = self.user
        ttl = {}

        if self.last_name and self.first_name:
            ttl['first_name'] = self.first_name
            ttl['last_name'] = self.last_name
        elif user:
            if user.last_name and user.first_name:
                ttl['first_name'] = user.first_name
                ttl['last_name'] = user.last_name
            ttl['username'] = user.username

        if ttl.get('first_name'):
            if ttl.get('username'):
                return "%(first_name)s %(last_name)s [%(username)s]" % ttl
            else:
                return "%(first_name)s %(last_name)s" % ttl
        elif ttl.get('username'):
            return "%(username)s" % ttl
        else:
            return "Employee №[%d]" % self.id

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        unique_together = (('user', 'company'),)
