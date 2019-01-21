from index.base.repository import Base


class UserRepository(Base):
    from .model import User as Model
    from .admin import User as Admin
    from .serializer import User as Basic
    from .validator import Register, Update

    model = Model
    admin = Admin

    serializers = {
        'base': Basic,
    }

    forms = {
        'register': Register,
        'update': Update,
    }
