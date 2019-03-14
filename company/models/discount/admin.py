from index.base.repository import Base


class DiscountAdmin(Base.Admin):
    list_display = ('name', 'percent')
