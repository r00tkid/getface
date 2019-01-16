from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.admin import ModelAdmin
from django.utils.html import format_html
from . import models

# Remove default groups
admin.site.unregister(Group)


class UserAdmin(ModelAdmin):
    list_display = (
        'display_full_name',
        'email',
        'display_is_active',
        'display_is_staff',
        'display_is_super',
        'display_id'
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

        return format_html(name)

    display_full_name.short_description = "ФИО"

    def display_id(self, obj):
        return obj.id

    display_id.short_description = "№"

    def display_is_staff(self, obj):
        if obj.is_staff:
            is_ok = "<span class='glyphicon glyphicon-ok' style='color: #262;'></span>"
        else:
            is_ok = "<span class='glyphicon glyphicon-remove' style='color: #922'></span>"

        return format_html(is_ok)

    display_is_staff.short_description = "Сотрудник"

    def display_is_super(self, obj):
        if obj.is_superuser:
            is_ok = "<span class='glyphicon glyphicon-ok' style='color: #262'></span>"
        else:
            is_ok = "<span class='glyphicon glyphicon-remove' style='color: #922'></span>"

        return format_html(is_ok)

    display_is_super.short_description = "Админ"

    def display_is_active(self, obj):
        if obj.is_active:
            is_ok = "<span class='glyphicon glyphicon-ok' style='color: #262'></span>"
        else:
            is_ok = "<span class='glyphicon glyphicon-remove' style='color: #922'></span>"

        return format_html(is_ok)

    display_is_active.short_description = "Актив"


# Add our user to admin panel
admin.site.register(models.User, UserAdmin)
