from index.base.repository import Base


class Discount(Base.Admin):
    list_display = ('name', 'percent')
