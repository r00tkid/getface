class Repository:
    from .model import Agenda as __Model
    from .admin import AgendaAdmin as __Admin

    model = __Model
    admin = __Admin

    class serializers:
        from .serializer import AgendaSerializer as __Serializer

        base = __Serializer

    class validators:
        from .validator import (
            AgendaCreateValidator as __Create,
            AgendaUpdateValidator as __Update
        )

        create = __Create
        update = __Update
