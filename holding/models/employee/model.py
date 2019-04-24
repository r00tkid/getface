from app.base.model import Model as _Model


class Employee(_Model):
    from django.db.models import fields as _field
    from app.fields import timezone as _timezone
    from django.db.models.fields import related as _related
    from django.db.models import deletion as _deletion

    first_name = _field.CharField(
        max_length=200,
        verbose_name="Имя",
    )

    last_name = _field.CharField(
        max_length=200,
        verbose_name="Фамилия",
    )

    phone = _field.CharField(
        max_length=200,
        verbose_name="Телефон",
        null=True,
        blank=True,
    )

    company = _related.ForeignKey(
        'holding.Company',
        on_delete=_deletion.SET_NULL,
        verbose_name="Компания",
        null=True,
        blank=True,
        related_name="employees",
    )

    is_manager = _field.BooleanField(
        verbose_name="Менеджер",
        default=False,
    )

    is_fired = _field.BooleanField(
        verbose_name="Уволен",
        default=False,
    )

    import uuid as _uuid
    auth_key = _field.UUIDField(
        verbose_name="Уникальный авторизационный ключ",
        editable=False,
        unique=True,
        null=True,
        blank=False,
        default=_uuid.uuid4,
    )

    email = _field.EmailField(
        verbose_name="E-mail",
        null=True,
        blank=True,
    )

    timezone = _timezone.TimeZoneField(
        verbose_name="Пояс",
        default="UTC",
        null=False,
        blank=True,
    )

    invitation = _field.DateTimeField(
        verbose_name="Последнее приглашение",
        null=True,
        blank=True,
    )

    is_invited = _field.BooleanField(
        verbose_name="Приглашён",
        null=False,
        default=False,
    )

    is_active = _field.BooleanField(
        verbose_name="Активен",
        null=False,
        default=False,
    )

    face_id = _field.UUIDField(
        verbose_name="Face ID",
        null=True,
        blank=True,
    )

    user = _related.ForeignKey(
        'entry.User',
        on_delete=_deletion.CASCADE,
        verbose_name="Физический пользователь",
        null=True,
        blank=True,
    )

    department = _related.ForeignKey(
        'holding.Department',
        on_delete=_deletion.SET_NULL,
        default=None,
        null=True,
        blank=True,
        related_name="employees",
    )

    position = _related.ForeignKey(
        'holding.Position',
        on_delete=_deletion.SET_NULL,
        default=None,
        null=True,
        blank=True,
        related_name="employees",
    )

    def clear_face_id(self):
        self.face_id = None

    def new_face_id(self):
        self.face_id = self._uuid.uuid4()

    def new_invitation(self):
        from datetime import datetime

        old = self.invitation
        self.invitation = datetime.now()
        return old

    def activate(self):
        self.is_invited = True
        self.is_active = True
        self.auth_key = None

    def __str__(self):
        user = self.user
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

    @classmethod
    def create_from_user(cls, user, **kwargs):
        """
        :type user: entry.models.User
        """
        from factory.faker import faker

        fake = faker.Faker(locale='ru_RU')

        employee = cls(
            user=user,

            first_name=user.first_name if user.first_name else fake.first_name(),
            last_name=user.last_name if user.last_name else fake.last_name(),
            timezone=user.timezone,
            phone=user.phone,
            email=user.email,
            is_active=True,
            **kwargs
        )

        employee.save()

        return employee

    def set_position(self, position, department=None):
        self.position = position

        if not department and not self.department:
            related = position.departments.first()

            if related:
                self.department = related.department
        elif department:
            self.department = department

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        unique_together = (('user', 'company'),)

    def create_user(self, username=None):
        """
        Creates user from employee, save it and send email if application not in debug mode
        :type username: str
        """
        from django.conf import settings
        from entry.models import User

        if not self.auth_key and not username:
            raise AttributeError('No username provided or can\'t be get from auth')

        user = User(
            username=username if username else self.auth_key,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            phone=self.phone,
            timezone=self.timezone,
        )

        user.save()
        self.user = user

        if user.email and not settings.DEBUG:
            user.mail_activation()

        if settings.DEBUG:
            user.activate()
            self.activate()

        return user
