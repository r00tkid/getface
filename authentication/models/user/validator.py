from index.base.repository import Base
from authentication.models.user.model import User


class UserCreateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    username = field.String('Username', [
        validation.Unique(User),
        validation.DataRequired(),
        validation.Length(min=6, max=200, message="Username must bee more than 5 and less than 201 characters."),
    ], description="Enter your username")

    email = field.String('E-mail', [
        validation.DataRequired(),
        validation.Length(min=5, max=200, message="E-mail must bee more than 4 and less than 201 characters."),
        validation.Email(message="E-mail must be valid email address"),
        validation.Unique(User, message="E-mail not unique")
    ])

    phone = field.String('Phone', [
        validation.DataRequired(),
        validation.Length(min=5, max=30, message="E-mail must bee more than 4 and less than 201 characters."),
        validation.Unique(User, message="Phone is already in use"),
    ])

    last_name = field.String('Last name', [
        validation.DataRequired(),
        validation.Length(min=2, max=200, message="Last name must bee more than 1 and less than 201 characters."),
    ], description="Enter your last name")

    first_name = field.String('First name', [
        validation.DataRequired(),
        validation.Length(min=2, max=200, message="First name must bee more than 1 and less than 201 characters."),
    ], description="Enter your first name")

    password = field.Password('Your password', [
        validation.DataRequired(),
        validation.Length(min=6, max=100, message="Password must bee more than 5 and less than 101 characters."),
        validation.EqualTo('password_confirmation', message="Passwords not match"),
    ])

    password_confirmation = field.Password(
        'Confirm password',
        [validation.DataRequired()],
        description="Confirm your password"
    )


class UserUpdateValidator(Base.Validator):
    pass
