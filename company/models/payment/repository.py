class Repository:
    from .model import Payment as __Model
    from .admin import PaymentAdmin as __Admin

    model = __Model
    admin = __Admin

    class serializers:
        from .serializer import PaymentSerializer as __Serializer

        base = __Serializer

    class validators:
        from .validator import PaymentCreateValidator as __Create

        create = __Create
