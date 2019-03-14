class Repository:
    from .model import Position as __Model

    model = __Model

    class serializers:
        from .serializer import PositionSerializer as __Serializer

        base = __Serializer

    class validators:
        from .validator import (
            PositionCreateValidator as __Create,
            PositionUpdateValidator as __Update
        )

        create = __Create
        update = __Update
