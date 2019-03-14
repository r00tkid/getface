class Repository:
    from .model import Feature as __Model
    from .admin import FeatureAdmin as __Admin

    model = __Model
    admin = __Admin

    class serializers:
        from .serializer import FeatureSerializer as __Serializer

        base = __Serializer

    class validators:
        from .validator import (
            FeatureCreateValidator as __Create,
            FeatureUpdateValidator as __Update
        )

        create = __Create
        update = __Update
