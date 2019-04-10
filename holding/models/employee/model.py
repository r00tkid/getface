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

    from holding.models import Company as _Company
    company = _related.ForeignKey(
        _Company,
        on_delete=_deletion.CASCADE,
        verbose_name="Компания",
        null=False,
        blank=False,
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
        verbose_name="Локальное время работника",
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

    from entry.models import User as _User
    user = _related.ForeignKey(
        _User,
        on_delete=_deletion.CASCADE,
        verbose_name="Физический пользователь",
        null=True,
        blank=True,
    )

    from holding.models import Department as _Department
    department = _related.ForeignKey(
        _Department,
        on_delete=_deletion.SET_NULL,
        default=None,
        null=True,
        blank=True,
        related_name="employees",
    )

    from holding.models import Position as _Position
    position = _related.ForeignKey(
        _Position,
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

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        unique_together = (('user', 'company'),)
