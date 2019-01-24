from index.base.repository import Base


class DiscountRepository(Base):

    @classmethod
    def model(cls):
        from .model import Discount

        return Discount

    @classmethod
    def admin_view(cls):
        from .admin import Discount

        return Discount

    @classmethod
    def actions(cls):
        from .validator import Create

        return {
            'create': Create,
        }

    @classmethod
    def serializers(cls):
        from .serializer import BaseDiscount

        return {
            'base': BaseDiscount,
        }
