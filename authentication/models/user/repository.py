class Repository:
    from .model import User as __Model
    from .admin import UserAdmin as __Admin

    model = __Model
    admin = __Admin

    class serializers:
        from .serializer import (
            UserSerializer as __Serializer,
            UserExtendedSerializer as __Extended
        )

        base = __Serializer
        extended = __Extended

    class validators:
        from .validator import (
            UserCreateValidator as __Create,
            UserUpdateValidator as __Update
        )

        create = __Create
        update = __Update
