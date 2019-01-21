class UserRepository(Base):
    model = User
    serializer = UserSerializer
    admin = UserAdmin

    forms = {
        'register': UserRegister,
        'update': UserUpdate,
    }


