from app.base.model import Model as _Model


class Progress(_Model):
    from django.db.models.fields import related as _related
    from django.db.models import deletion as _deletion

    user = _related.ForeignKey(
        'entry.User',
        on_delete=_deletion.CASCADE,
        verbose_name="Пользователь",
        null=False,
        blank=False,
    )

    feature = _related.ForeignKey(
        'entry.Feature',
        on_delete=_deletion.CASCADE,
        verbose_name="Фича",
        null=False,
        blank=False,
    )

    def __str__(self):
        return "Прогресс по %s для пользователя %s" % (self.feature, self.user)

    class Meta:
        verbose_name = 'Прогресс'
        verbose_name_plural = 'Прогресс'
