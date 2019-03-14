from index.base.repository import Base


class PaymentAdmin(Base.Admin):
    list_display = ('company', 'user', 'rate', 'discount')
