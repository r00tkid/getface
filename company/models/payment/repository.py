import typing as tp
from index.base.repository import Base


class PaymentRepository(Base):
    from .model import Payment as __Model
    from .admin import Payment as __Admin
    from .validator import Create as __Create
    from .serializer import BasePayment as __BasePayment

    @classmethod
    def model(cls) -> tp.Type[__Model]:
        return cls.__Model

    @classmethod
    def admin_view(cls) -> tp.Type[__Admin]:
        return cls.__Admin

    @classmethod
    def actions(cls) -> tp.Dict[str, tp.Union[tp.Type[__Create]]]:
        return {
            'create': cls.__Create,
        }

    @classmethod
    def serializers(cls) -> tp.Dict[str, tp.Union[tp.Type[__BasePayment]]]:
        return {
            'base': cls.__BasePayment,
        }
