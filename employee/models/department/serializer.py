from index.base.repository import Base
from .model import Department


class BaseDepartment(Base.Serializer):
    class Meta:
        model = Department
        fields = ('name', 'company', 'id',)
