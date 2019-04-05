from authentication.models.feature.model import Feature
from authentication.models.user.model import User
from index.base.repository import Base


class Progress(Base.models.CreatedStump):
    relation = Base.models.Model.relation
    field = Base.models.Model.field

    user = field.foreign(
        User,
        on_delete=relation.cascade,
        verbose_name="Пользователь",
        null=False,
        blank=False,
    )

    feature = field.foreign(
        Feature,
        on_delete=relation.cascade,
        verbose_name="Фича",
        null=False,
        blank=False,
    )

    def __str__(self):
        return "Прогресс по %s для пользователя %s" % (self.feature, self.user)

    class Meta:
        verbose_name = 'Прогресс'
        verbose_name_plural = 'Прогресс'
