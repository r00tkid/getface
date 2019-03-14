from index.base.repository import Base


class RateAdmin(Base.Admin):
    list_display = ('name', 'per_month', 'is_archived', 'id')
