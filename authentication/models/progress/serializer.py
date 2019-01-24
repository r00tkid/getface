from index.base.repository import Base
from .model import Progress


class BaseProgress(Base.Serializer):
    class Meta:
        model = Progress
        fields = ('user', 'feature')
