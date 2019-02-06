from index.base.repository import Base
from .model import WorkerPosition


class BasePosition(Base.Serializer):
    class Meta:
        model = WorkerPosition
        fields = ('name', 'company', 'id')
