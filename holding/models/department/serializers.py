from rest_framework.serializers import ModelSerializer as _Serializer


class DepartmentSerializer(_Serializer):
    class Meta:
        from .model import Department as _Department

        model = _Department
        fields = ('name', 'company', 'id',)
