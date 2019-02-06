from index.base.repository import Base
from authentication.models import User
from .model import Employee


class Register(Base.Validator):
    field = Base.Validator.field
    valid = Base.Validator.valid

    uuid = field.Hidden('Auth key [hidden]', [
        valid.ValidationChain(
            valid.UUID(message="Invalid or not provided secret key."),
            valid.Exists(
                Employee,
                column="auth_key",
                message="Secret key not found or expired. Make sure that you still have invitation to system."
            ),
        )
    ])

    username = field.String('Username', [
        valid.Unique(User.model()),
        valid.DataRequired(),
        valid.Length(min=6, max=200, message="Username must bee more than 5 and less than 201 characters."),
    ], description="Enter your username")

    password = field.Password('Your password', [
        valid.DataRequired(),
        valid.EqualTo('password_confirmation', message="Passwords not match"),
        valid.Length(min=6, max=100, message="Password must bee more than 5 and less than 101 characters."),
    ])

    password_confirmation = field.Password(
        'Confirm password',
        [valid.DataRequired()],
        description="Confirm your password"
    )


class Create(Base.Validator):
    field = Base.Validator.field
    valid = Base.Validator.valid

    last_name = field.String('Last name', [
        valid.DataRequired(),
        valid.Length(min=2, max=200, message="Last name length must be between 2 and 200 characters inclusive."),
    ], description="Enter your last name")

    first_name = field.String('First name', [
        valid.DataRequired(),
        valid.Length(min=2, max=200, message="First name length must be between 2 and 200 characters inclusive."),
    ], description="Enter your first name")

    email = field.String('E-mail', [
        valid.DataRequired(),
        valid.Length(min=6, max=200, message="E-mail length must be between 6 and 200 characters inclusive."),
        valid.Email(message="E-mail must be valid email address"),
    ])

    phone = field.String('Phone', [
        valid.NotRequired(),
        valid.Length(min=6, max=30, message="Phone length must be between 6 and 30 characters inclusive."),
    ])


class Update(Base.Validator):
    field = Base.Validator.field
    valid = Base.Validator.valid

    last_name = field.String('Last name', [
        valid.NotRequired(allow_empty=False),
        valid.Length(min=2, max=200, message="Last name length must be between 2 and 200 characters inclusive."),
    ], description="Enter your last name")

    first_name = field.String('First name', [
        valid.NotRequired(allow_empty=False),
        valid.Length(min=2, max=200, message="First name length must be between 2 and 200 characters inclusive."),
    ], description="Enter your first name")

    email = field.String('E-mail', [
        valid.NotRequired(),
        valid.Length(min=6, max=200, message="E-mail length must be between 6 and 200 characters inclusive."),
        valid.Email(message="E-mail must be valid email address"),
    ])

    phone = field.String('Phone', [
        valid.NotRequired(),
        valid.Length(min=6, max=30, message="Phone length must be between 6 and 30 characters inclusive."),
    ])
