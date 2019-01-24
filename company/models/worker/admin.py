from index.base.repository import Base

format_html = Base.Admin.format_html


class Worker(Base.Admin):
    list_display = ('display_full_name', 'display_email', 'display_auth_key',
                    'display_is_active', 'display_id', 'auth_key')

    def display_id(self, obj):
        return obj.id

    display_id.short_description = "№"

    def display_full_name(self, obj):
        full = "%s %s" % (obj.first_name, obj.last_name) + (
            " (%s)" % obj.user.username if obj.user_id else ""
        )

        if obj.is_manager:
            full += " <span class='label label-success'>%s</span>" % "Менеджер"

        if obj.is_fired:
            full += " <span class='label label-danger'>%s</span>" % "Уволен"

        if obj.user:
            if obj.user.is_staff:
                full += " <span class='label label-info'>%s</span>" % "Сотрудник"
            if obj.user.is_superuser:
                full += " <span class='label label-primary'>%s</span>" % "Администратор"

        return format_html(full)

    display_full_name.short_description = "ФИО"

    def display_email(self, obj):
        return obj.user.email if (obj.user and obj.user.email) else None

    display_email.short_description = "E-mail"

    def display_auth_key(self, obj):
        if obj.auth_key:
            return format_html(
                "<span class='glyphicon glyphicon-remove' style='color: #922;'></span>"
            )
        else:
            return format_html(
                "<span class='glyphicon glyphicon-ok' style='color: #262;'></span>"
            )

    display_auth_key.short_description = "Инвайт"

    def display_is_active(self, obj):
        if obj.user and obj.user.is_active:
            return format_html(
                "<span class='glyphicon glyphicon-ok' style='color: #262;'></span>"
            )
        else:
            return format_html(
                "<span class='glyphicon glyphicon-remove' style='color: #922;'></span>"
            )

    display_is_active.short_description = "Актив"
