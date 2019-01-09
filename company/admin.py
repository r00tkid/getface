from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Company, Worker

from django.utils.html import format_html


class WorkerAdmin(ModelAdmin):
    list_display = ('display_full_name', 'display_email', 'id')

    def display_full_name(self, obj):
        full = "%s %s" % (obj.first_name, obj.last_name) + (
            " (%s)" % obj.user.username if obj.user_id else ""
        )

        if obj.is_manager:
            full += " [<span style='color: #771;'>%s</span>]" % "Менеджер"

        if obj.user:
            if obj.user.is_staff:
                full += " [<span style='color: #222298;'>%s</span>]" % "Сотрудник"
            if obj.user.is_superuser:
                full += " [<span style='color: #982222;'>%s</span>]" % "Администратор"

        return format_html(full)

    display_full_name.short_description = "ФИО"

    def display_email(self, obj):
        return obj.user.email if obj.user else None

    display_email.short_description = "E-mail"


admin.site.register(Company)
admin.site.register(Worker, WorkerAdmin)
