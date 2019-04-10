from app.base.model import Model as _Model


class Feature(_Model):
    from django.db.models import fields as _field

    name = _field.CharField(
        "Название",
        max_length=256,
        null=False,
        blank=False,
    )

    link = _field.CharField(
        "Ссылка",
        max_length=1024,
        null=True,
        blank=True,
    )

    description = _field.TextField(
        "Описание",
        max_length=5000,
        null=False,
        blank=False,
    )

    is_alive = _field.BooleanField(
        "Существует",
        default=True,
    )

    is_important = _field.BooleanField(
        "Важная",
        default=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фича'
        verbose_name_plural = 'Фичи'
