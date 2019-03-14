from index.base.repository import Base
from .model import Department


class DepartmentSerializer(Base.Serializer):
    class Meta:
        model = Department
        fields = ('name', 'company', 'id',)
