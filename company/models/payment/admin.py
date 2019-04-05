from index.base.repository import Base


class PaymentAdmin(Base.Admin):
    list_display = ('company', 'user', 'rate', 'discount',)


class PaymentDetailsAdmin(Base.Admin):
    list_display = ('display_special_details_name', 'rate', 'display_discount', 'start',)

    def display_special_details_name(self, details):
        company = details.company.name
        user = details.payment.user  # Reverse relationship

        return "№%d \"%s\" от %s (%s)" % (details.id, company, user, details.created_at.strftime("%Y-%m-%d %H:%M:%S [%Z]"))

    display_special_details_name.short_description = "Оплата"

    def display_discount(self, details):
        return str(details.discount)

    display_discount.short_description = "Скидка"
