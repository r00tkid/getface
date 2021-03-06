from entry.models.progress.model import Progress as _Progress
from django.contrib.admin import ModelAdmin as _Admin
from django.utils.html import format_html as _format


class UserAdmin(_Admin):
    list_display = (
        'display_full_name',
        'email',
        'phone',
        'display_is_active',
        'display_is_staff',
        'display_is_super',
        'display_achieves',
        'activation',
        'is_banned',
        'display_id',
    )

    def display_full_name(self, obj):
        if obj.first_name or obj.last_name:
            name = obj.first_name if obj.first_name else ''
            name += " " if obj.first_name and obj.last_name else ''
            name += obj.last_name if obj.last_name else ''
            name += " " if obj.last_name else ''
            name += "<span class='label' style='border-radius: 20rem;background-color: #666'>%s</span>" % obj.username
        else:
            name = obj.username

        return _format(name)

    display_full_name.short_description = "ФИО"

    def display_id(self, obj):
        return obj.id

    display_id.short_description = "№"

    def display_is_staff(self, obj):
        if obj.is_staff:
            is_ok = "<span class='glyphicon glyphicon-ok' style='color: #262;'></span>"
        else:
            is_ok = "<span class='glyphicon glyphicon-remove' style='color: #922'></span>"

        return _format(is_ok)

    display_is_staff.short_description = "Сотрудник"

    def display_is_super(self, obj):
        if obj.is_superuser:
            is_ok = "<span class='glyphicon glyphicon-ok' style='color: #262'></span>"
        else:
            is_ok = "<span class='glyphicon glyphicon-remove' style='color: #922'></span>"

        return _format(is_ok)

    display_is_super.short_description = "Админ"

    def display_is_active(self, obj):
        if obj.is_active:
            is_ok = "<span class='glyphicon glyphicon-ok' style='color: #262'></span>"
        else:
            is_ok = "<span class='glyphicon glyphicon-remove' style='color: #922'></span>"

        return _format(is_ok)

    display_is_active.short_description = "Актив"

    def display_achieves(self, obj):
        return _Progress.objects.filter(user=obj, feature__is_alive=True).count()

    display_achieves.short_description = "Достижений"
