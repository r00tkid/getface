from .user import User
from .feature import Feature
from index.base.repository import Base


class Progress(Base.TimeStumps, Base.SoftDeletion):
    field = Base.Model.field
    rel = Base.Model.rel

    user = field.Foreign(
        User,
        on_delete=rel.CASCADE,
        verbose_name="Пользователь",
        null=False,
        blank=False,
    )

    feature = field.Foreign(
        Feature,
        on_delete=rel.CASCADE,
        verbose_name="Фича",
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = 'Прогресс'
        verbose_name_plural = 'Прогресс'
