from index.base.repository import Base


class PaymentRepository(Base):

    @classmethod
    def model(cls):
        from .model import Payment

        return Payment

    @classmethod
    def admin_view(cls):
        from .admin import Payment

        return Payment

    @classmethod
    def actions(cls):
        from .validator import Create, Update

        return {
            'create': Create,
            'update': Update
        }

    @classmethod
    def serializers(cls):
        from .serializer import BasePayment, ExtendedPayment

        return {
            'base': BasePayment,
            'extended': ExtendedPayment,
        }
