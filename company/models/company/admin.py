from index.base.repository import Base


class CompanyAdmin(Base.Admin):
    list_display = ('name', 'created_at', 'timezone', 'time_left', 'rate', 'id',)
