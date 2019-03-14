from index.base.repository import Base
from authentication.models.user.model import User


class UserCreateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    username = field.string('Username', [
        validation.unique(User),
        validation.data_required(),
        validation.length(min=6, max=200, message="Username must bee more than 5 and less than 201 characters."),
    ], description="Enter your username")

    email = field.string('E-mail', [
        validation.data_required(),
        validation.length(min=5, max=200, message="E-mail must bee more than 4 and less than 201 characters."),
        validation.email(message="E-mail must be valid email address"),
        validation.unique(User, message="E-mail not unique")
    ])

    phone = field.string('Phone', [
        validation.data_required(),
        validation.length(min=5, max=30, message="E-mail must bee more than 4 and less than 201 characters."),
        validation.unique(User, message="Phone is already in use"),
    ])

    last_name = field.string('Last name', [
        validation.data_required(),
        validation.length(min=2, max=200, message="Last name must bee more than 1 and less than 201 characters."),
    ], description="Enter your last name")

    first_name = field.string('First name', [
        validation.data_required(),
        validation.length(min=2, max=200, message="First name must bee more than 1 and less than 201 characters."),
    ], description="Enter your first name")

    password = field.password('Your password', [
        validation.data_required(),
        validation.length(min=6, max=100, message="Password must bee more than 5 and less than 101 characters."),
        validation.equal_to('password_confirmation', message="Passwords not match"),
    ])

    password_confirmation = field.password(
        'Confirm password',
        [validation.data_required()],
        description="Confirm your password"
    )


class UserUpdateValidator(Base.Validator):
    pass
