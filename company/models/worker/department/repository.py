import typing as tp
from index.base.repository import Base


class DepartmentRepository(Base):
    from .model import WorkerDepartment as __Model
    from .validator import Create as __Create, Update as __Update
    from .serializer import BaseDepartment as __BaseDepartment

    @classmethod
    def model(cls) -> tp.Type[__Model]:
        return cls.__Model

    @classmethod
    def admin_view(cls):
        raise NotImplemented

    @classmethod
    def actions(cls) -> tp.Dict[str, tp.Union[tp.Type[__Create], tp.Type[__Update]]]:
        return {
            'create': cls.__Create,
            'update': cls.__Update,
        }

    @classmethod
    def serializers(cls) -> tp.Dict[str, tp.Union[tp.Type[__BaseDepartment]]]:
        return {
            'base': cls.__BaseDepartment,
        }
