from index.base.repository import Base


class Agenda(Base.Admin):
    list_display = ('display_worker_company', 'display_date', 'display_time_range', 'active', 'mood', 'fatigue',)

    def display_worker_company(self, obj):
        """
        :type obj: agenda.models.calendar.model.Calendar
        """
        worker = obj.employee
        company = worker.company

        return "%s [%s]" % (company.name, str(worker))

    def display_time_range(self, obj):
        """
        :type obj: agenda.models.calendar.model.Calendar
        """
        return "%s - %s" % (obj.start.time(), obj.end.time())

    def display_date(self, obj):
        """
        :type obj: agenda.models.calendar.model.Calendar
        """
        return obj.start.date()

    display_worker_company.short_description = "Компания [Работник]"
    display_time_range.short_description = "Время"
    display_date.short_description = "Дата"
