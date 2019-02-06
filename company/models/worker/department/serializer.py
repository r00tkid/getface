from index.base.repository import Base
from .model import WorkerDepartment


class BaseDepartment(Base.Serializer):
    class Meta:
        model = WorkerDepartment
        fields = ('name', 'company', 'id',)
