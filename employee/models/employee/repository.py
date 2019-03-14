class Repository:
    from .model import Employee as __Model
    from .admin import EmployeeAdmin as __Admin

    model = __Model
    admin = __Admin

    class serializers:
        from .serializer import (
            EmployeeSerializer as __Serializer,
            EmployeeExtendedSerializer as __Extended,
        )

        base = __Serializer
        extended = __Extended

    class validators:
        from .validator import (
            EmployeeCreateValidator as __Create,
            EmployeeActivateValidator as __Activate,
            EmployeeUpdateValidator as __Update,
        )

        create = __Create
        activate = __Activate
        update = __Update
