import typing as tp
from index.base.repository import Base


class EmployeeRepository(Base):
    from .model import Employee as __Model
    from .admin import Employee as __Admin
    from .validator import Register as __Register, Create as __Create, Update as __Update
    from .serializer import BaseEmployee as __BaseEmployee, ExtendedEmployee as __ExtendedEmployee

    @classmethod
    def model(cls) -> tp.Type[__Model]:
        return cls.__Model

    @classmethod
    def admin_view(cls) -> tp.Type[__Admin]:
        return cls.__Admin

    @classmethod
    def actions(cls) -> tp.Dict[str, tp.Union[tp.Type[__Register], tp.Type[__Create], tp.Type[__Update]]]:
        return {
            'register': cls.__Register,
            'create': cls.__Create,
            'update': cls.__Update,
        }

    @classmethod
    def serializers(cls) -> tp.Dict[str, tp.Union[tp.Type[__BaseEmployee], tp.Type[__ExtendedEmployee]]]:
        return {
            'base': cls.__BaseEmployee,
            'extended': cls.__ExtendedEmployee,
        }
