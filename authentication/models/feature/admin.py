from authentication.models.progress.model import Progress
from index.base.repository import Base


class FeatureAdmin(Base.Admin):
    format_html = Base.Admin.format_html

    list_display = (
        'name',
        'link',
        'is_alive',
        'is_important',
        'display_achieved',
    )

    def display_achieved(self, obj):
        """
        :type obj: authentication.models.feature.model.Feature
        """
        return Progress.objects.filter(feature=obj).count()

    display_achieved.short_description = "Достигнуто раз"
