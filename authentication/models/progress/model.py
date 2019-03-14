from index.base.repository import Base
from authentication.models.user.model import User
from authentication.models.feature.model import Feature


class Progress(Base.models.CreatedStump):
    relations = Base.models.Model.relations
    field = Base.models.Model.field

    user = field.Foreign(
        User,
        on_delete=relations.CASCADE,
        verbose_name="Пользователь",
        null=False,
        blank=False,
    )

    feature = field.Foreign(
        Feature,
        on_delete=relations.CASCADE,
        verbose_name="Фича",
        null=False,
        blank=False,
    )

    def __str__(self):
        return "Прогресс по %s для пользователя %s" % (self.feature, self.user)

    class Meta:
        verbose_name = 'Прогресс'
        verbose_name_plural = 'Прогресс'
