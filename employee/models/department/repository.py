class Repository:
    from .model import Department as __Model

    model = __Model

    class serializers:
        from .serializer import DepartmentSerializer as __Serializer

        base = __Serializer

    class validators:
        from .validator import (
            DepartmentCreateValidator as __Create,
            DepartmentUpdateValidator as __Update
        )

        create = __Create
        update = __Update
