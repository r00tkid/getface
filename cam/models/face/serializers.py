from rest_framework.serializers import ModelSerializer as _Serializer


class FaceSerializer(_Serializer):
    class Meta:
        from .model import Face as _

        model = _
        fields = ('id', 'employee_id', 'face_id')
