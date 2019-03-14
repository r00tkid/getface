class Repository:
    from .model import Calendar as __Model
    from .admin import CalendarAdmin as __Admin

    model = __Model
    admin = __Admin

    class serializers:
        from .serializer import CalendarSerializer as __Serializer

        base = __Serializer

    class validators:
        from .validator import (
            CalendarCreateValidator as __Create,
            CalendarUpdateValidator as __Update
        )

        create = __Create
        update = __Update
