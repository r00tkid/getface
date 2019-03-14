from index.base.repository import Base
from authentication.models import User
from .model import Employee


class EmployeeCreateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    last_name = field.string('Last name', [
        validation.data_required(),
        validation.length(min=2, max=200, message="Last name length must be between 2 and 200 characters inclusive."),
    ], description="Enter your last name")

    first_name = field.string('First name', [
        validation.data_required(),
        validation.length(min=2, max=200, message="First name length must be between 2 and 200 characters inclusive."),
    ], description="Enter your first name")

    email = field.string('E-mail', [
        validation.data_required(),
        validation.length(min=6, max=200, message="E-mail length must be between 6 and 200 characters inclusive."),
        validation.email(message="E-mail must be valid email address"),
    ])

    phone = field.string('Phone', [
        validation.not_required(),
        validation.length(min=6, max=30, message="Phone length must be between 6 and 30 characters inclusive."),
    ])


class EmployeeActivateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    uuid = field.hidden('Auth key [hidden]', [
        validation.validation_chain(
            validation.uuid(message="Invalid or not provided secret key."),
            validation.exists(
                Employee,
                column="auth_key",
                message="Secret key not found or expired. Make sure that you still have invitation to system."
            ),
        )
    ])

    username = field.string('Username', [
        validation.unique(User.model()),
        validation.data_required(),
        validation.length(min=6, max=200, message="Username must bee more than 5 and less than 201 characters."),
    ], description="Enter your username")

    password = field.password('Your password', [
        validation.data_required(),
        validation.equal_to('password_confirmation', message="Passwords not match"),
        validation.length(min=6, max=100, message="Password must bee more than 5 and less than 101 characters."),
    ])

    password_confirmation = field.password(
        'Confirm password',
        [validation.data_required()],
        description="Confirm your password"
    )


class EmployeeUpdateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    last_name = field.string('Last name', [
        validation.not_required(allow_empty=False),
        validation.length(min=2, max=200, message="Last name length must be between 2 and 200 characters inclusive."),
    ], description="Enter your last name")

    first_name = field.string('First name', [
        validation.not_required(allow_empty=False),
        validation.length(min=2, max=200, message="First name length must be between 2 and 200 characters inclusive."),
    ], description="Enter your first name")

    email = field.string('E-mail', [
        validation.not_required(),
        validation.length(min=6, max=200, message="E-mail length must be between 6 and 200 characters inclusive."),
        validation.email(message="E-mail must be valid email address"),
    ])

    phone = field.string('Phone', [
        validation.not_required(),
        validation.length(min=6, max=30, message="Phone length must be between 6 and 30 characters inclusive."),
    ])
