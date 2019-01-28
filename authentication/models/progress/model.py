from index.base.repository import Base
from authentication.models.user.model import User
from authentication.models.feature.model import Feature


class Progress(Base.CreatedStump):
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
