from index.base.repository import Base
from authentication.models.user.model import User


class Register(Base.Validator):
    field = Base.Validator.field
    valid = Base.Validator.valid

    username = field.String('Username', [
        valid.Unique(User),
        valid.DataRequired(),
        valid.Length(min=6, max=200, message="Username must bee more than 5 and less than 201 characters."),
    ], description="Enter your username")

    email = field.String('E-mail', [
        valid.DataRequired(),
        valid.Length(min=5, max=200, message="E-mail must bee more than 4 and less than 201 characters."),
        valid.Email(message="E-mail must be valid email address"),
        valid.Unique(User, message="E-mail not unique")
    ])

    phone = field.String('Phone', [
        valid.DataRequired(),
        valid.Length(min=5, max=30, message="E-mail must bee more than 4 and less than 201 characters."),
        valid.Unique(User, message="Phone is already in use"),
    ])

    last_name = field.String('Last name', [
        valid.DataRequired(),
        valid.Length(min=2, max=200, message="Last name must bee more than 1 and less than 201 characters."),
    ], description="Enter your last name")

    first_name = field.String('First name', [
        valid.DataRequired(),
        valid.Length(min=2, max=200, message="First name must bee more than 1 and less than 201 characters."),
    ], description="Enter your first name")

    password = field.Password('Your password', [
        valid.DataRequired(),
        valid.Length(min=6, max=100, message="Password must bee more than 5 and less than 101 characters."),
        valid.EqualTo('password_confirmation', message="Passwords not match"),
    ])

    password_confirmation = field.Password(
        'Confirm password',
        [valid.DataRequired()],
        description="Confirm your password"
    )


class Update(Base.Validator):
    pass
