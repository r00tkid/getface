from django.contrib.admin import ModelAdmin as _Admin


class FeatureAdmin(_Admin):
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
        from entry.models.progress.model import Progress as _Progress

        return _Progress.objects.filter(feature=obj).count()

    display_achieved.short_description = "Достигнуто раз"
