import uuid
from datetime import datetime
from index.base.repository import Base
from authentication.models.user.model import User
from company.models.company.model import Company

from employee.models.position.model import Position
from employee.models.department.model import Department


class Employee(Base.models.Model):
    relation = Base.models.Model.relation
    field = Base.models.Model.field

    first_name = field.char(
        max_length=200,
        verbose_name="Имя",
    )

    last_name = field.char(
        max_length=200,
        verbose_name="Фамилия",
    )

    phone = field.char(
        max_length=200,
        verbose_name="Телефон",
        null=True,
        blank=True,
    )

    company = field.foreign(
        Company,
        on_delete=relation.cascade,
        verbose_name="Компания",
        null=False,
        blank=False,
    )

    is_manager = field.boolean(
        verbose_name="Менеджер",
        default=False,
    )

    is_fired = field.boolean(
        verbose_name="Уволен",
        default=False,
    )

    auth_key = field.uuid(
        verbose_name="Уникальный авторизационный ключ",
        editable=False,
        unique=True,
        null=True,
        blank=False,
        default=uuid.uuid4,
    )

    email = field.email(
        verbose_name="E-mail",
        null=True,
        blank=True,
    )

    timezone = field.time_zone(
        verbose_name="Локальное время работника",
        default="UTC",
        null=False,
        blank=True,
    )

    invitation = field.date_time(
        verbose_name="Последнее приглашение",
        null=True,
        blank=True,
    )

    is_invited = field.boolean(
        verbose_name="Приглашён",
        null=False,
        default=False,
    )

    is_active = field.boolean(
        verbose_name="Активен",
        null=False,
        default=False,
    )

    face_id = field.uuid(
        verbose_name="Face ID",
        null=True,
        blank=True,
    )

    user = field.foreign(
        User,
        on_delete=relation.cascade,
        verbose_name="Физический пользователь",
        null=True,
        blank=True,
    )

    department = field.foreign(
        Department,
        on_delete=relation.set_null,
        default=None,
        null=True,
        blank=True,
    )

    position = field.foreign(
        Position,
        on_delete=relation.set_null,
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
