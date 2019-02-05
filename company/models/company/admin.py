from index.base.repository import Base


class Company(Base.Admin):
    format_html = Base.Admin.format_html

    list_display = ('name', 'created_at', 'timezone', 'id',)
