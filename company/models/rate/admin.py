from index.base.repository import Base


class Rate(Base.Admin):
    list_display = ('name', 'per_month', 'is_archived', 'id')
