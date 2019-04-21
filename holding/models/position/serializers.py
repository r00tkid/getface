from rest_framework.serializers import ModelSerializer as _Serializer


# ToDo: (Ack) update serializer
class PositionSerializer(_Serializer):
    class Meta:
        from .model import Position as _Position

        model = _Position
        fields = ('name', 'company', 'id')
