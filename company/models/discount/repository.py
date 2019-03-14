class Repository:
    from .model import Discount as __Model
    from .admin import DiscountAdmin as __Admin

    model = __Model
    admin = __Admin

    class serializers:
        from .serializer import DiscountSerializer as __Serializer

        base = __Serializer

    class validators:
        from .validator import DiscountCreateValidator as __Create

        create = __Create
