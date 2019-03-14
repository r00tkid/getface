class Repository:
    from .model import Company as __Model
    from .admin import CompanyAdmin as __Admin

    model = __Model
    admin = __Admin

    class serializers:
        from .serializer import (
            CompanySerializer as __Serializer,
            CompanyExtendedSerializer as __Extended
        )

        base = __Serializer
        extended = __Extended

    class validators:
        from .validator import (
            CompanyCreateValidator as __Create,
            CompanyUpdateValidator as __Update
        )

        create = __Create
        update = __Update
