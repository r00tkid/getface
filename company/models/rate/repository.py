class Repository:
    from .model import Rate as __Model
    from .admin import RateAdmin as __Admin

    model = __Model
    admin = __Admin

    class serializers:
        from .serializer import RateSerializer as __Serializer

        base = __Serializer

    class validators:
        from .validator import (
            RateCreateValidator as __Create,
            RateUpdateValidator as __Update
        )

        create = __Create
        update = __Update
