from app.base.model import Model as _Model


class Camera(_Model):
    from django.db.models.fields import related as _related
    from django.db.models import deletion as _deletion
    from django.db.models import fields as _field
    from app.fields import timezone as _timezone

    name = _field.CharField(
        verbose_name="Название",
        max_length=128,
        null=False,
        blank=False,
    )

    ip_address = _field.GenericIPAddressField(
        verbose_name="IP адрес",
        max_length=64,
    )

    login = _field.CharField(
        verbose_name="Логин",
        max_length=256,
        null=False,
        blank=False,
    )

    password = _field.CharField(
        verbose_name="Пароль",
        max_length=256,
        null=False,
        blank=True,
        default="",
    )

    is_active = _field.BooleanField(
        verbose_name="Активна",
        null=False,
        blank=False,
        default=True,
    )

    company = _related.ForeignKey(
        'holding.Company',
        on_delete=_deletion.CASCADE,
        null=False,
        blank=False,
        related_name="cameras",
    )

    zone = _related.ForeignKey(
        'cam.Zone',
        on_delete=_deletion.SET_NULL,
        null=True,
        blank=True,
        related_name="cameras",
    )

    timezone = _timezone.TimeZoneField(
        "Временная зона",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Камера"
        verbose_name_plural = "Камеры"
