from index.base.repository import Base


class UserRepository(Base):
    from . import model, admin, serializer, validator
