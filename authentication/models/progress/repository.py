class Repository:
    from .model import Progress as __Model
    from .admin import ProgressAdmin as __Admin

    model = __Model
    admin = __Admin

    class serializers:
        from .serializer import ProgressSerializer as __Serializer

        base = __Serializer

    class validators:
        from .validator import ProgressCreateValidator as __Create

        create = __Create
