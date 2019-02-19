from index.base.repository import Base


class Payment(Base.Admin):
    list_display = ('company', 'user', 'rate', 'discount')
