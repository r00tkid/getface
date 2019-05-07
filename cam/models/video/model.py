from app.base.model import Model as _Model


class Video(_Model):
    from django.db.models.fields import related as _related
    from django.db.models import deletion as _deletion
    from django.db.models import fields as _field

    start = _field.DateTimeField("Начало")
    duration = _field.DurationField("Продолжительность")

    filename = _field.CharField(
        verbose_name="Название файла",
        max_length=128,
        null=False,
        blank=False,
    )

    # There is need to be link to file

    camera = _related.ForeignKey(
        'cam.Camera',
        on_delete=_deletion.CASCADE,
        null=False,
        blank=False,
    )

    @property
    def timezone(self):
        return self.camera.timezone if self.camera.timezone else self.camera.company.timezone

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"
