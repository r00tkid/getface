from django.contrib.admin import ModelAdmin as _Admin


class PositionAdmin(_Admin):
    from holding.models import Employee as _Employee

    list_display = (
        'name',
        'company',
        'display_employees_amount',
        'id',
    )

    def display_employees_amount(self, position):
        return self._Employee.objects.filter(position=position).count()

    display_employees_amount.short_description = "Кол-во сотрудников"
