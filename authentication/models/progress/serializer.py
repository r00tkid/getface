from index.base.repository import Base
from .model import Progress


class ProgressSerializer(Base.Serializer):
    class Meta:
        model = Progress
        fields = ('user', 'feature')
