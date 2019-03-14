from index.base.repository import Base
from authentication.models import User
from .model import Employee


class EmployeeCreateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    last_name = field.String('Last name', [
        validation.DataRequired(),
        validation.Length(min=2, max=200, message="Last name length must be between 2 and 200 characters inclusive."),
    ], description="Enter your last name")

    first_name = field.String('First name', [
        validation.DataRequired(),
        validation.Length(min=2, max=200, message="First name length must be between 2 and 200 characters inclusive."),
    ], description="Enter your first name")

    email = field.String('E-mail', [
        validation.DataRequired(),
        validation.Length(min=6, max=200, message="E-mail length must be between 6 and 200 characters inclusive."),
        validation.Email(message="E-mail must be valid email address"),
    ])

    phone = field.String('Phone', [
        validation.NotRequired(),
        validation.Length(min=6, max=30, message="Phone length must be between 6 and 30 characters inclusive."),
    ])


class EmployeeActivateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    uuid = field.Hidden('Auth key [hidden]', [
        validation.ValidationChain(
            validation.UUID(message="Invalid or not provided secret key."),
            validation.Exists(
                Employee,
                column="auth_key",
                message="Secret key not found or expired. Make sure that you still have invitation to system."
            ),
        )
    ])

    username = field.String('Username', [
        validation.Unique(User.model()),
        validation.DataRequired(),
        validation.Length(min=6, max=200, message="Username must bee more than 5 and less than 201 characters."),
    ], description="Enter your username")

    password = field.Password('Your password', [
        validation.DataRequired(),
        validation.EqualTo('password_confirmation', message="Passwords not match"),
        validation.Length(min=6, max=100, message="Password must bee more than 5 and less than 101 characters."),
    ])

    password_confirmation = field.Password(
        'Confirm password',
        [validation.DataRequired()],
        description="Confirm your password"
    )


class EmployeeUpdateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    last_name = field.String('Last name', [
        validation.NotRequired(allow_empty=False),
        validation.Length(min=2, max=200, message="Last name length must be between 2 and 200 characters inclusive."),
    ], description="Enter your last name")

    first_name = field.String('First name', [
        validation.NotRequired(allow_empty=False),
        validation.Length(min=2, max=200, message="First name length must be between 2 and 200 characters inclusive."),
    ], description="Enter your first name")

    email = field.String('E-mail', [
        validation.NotRequired(),
        validation.Length(min=6, max=200, message="E-mail length must be between 6 and 200 characters inclusive."),
        validation.Email(message="E-mail must be valid email address"),
    ])

    phone = field.String('Phone', [
        validation.NotRequired(),
        validation.Length(min=6, max=30, message="Phone length must be between 6 and 30 characters inclusive."),
    ])
