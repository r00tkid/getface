from wtforms import Form, StringField, PasswordField, HiddenField, validators
from form import base
from authentication.serializers import User
from company.models import Worker


class Registration(Form):
    # Owner block
    username = StringField('Username', [
        base.Unique(User),
        validators.DataRequired(),
        validators.Length(min=6, max=200, message="Username must bee more than 5 and less than 201 characters."),
    ], description="Enter your username")

    email = StringField('E-mail', [
        validators.DataRequired(),
        validators.Length(min=5, max=200, message="E-mail must bee more than 4 and less than 201 characters."),
        validators.Email(message="E-mail must be valid email address"),
        base.Unique(User, message="E-mail not unique")
    ])

    last_name = StringField('Last name', [
        validators.DataRequired(),
        validators.Length(min=2, max=200, message="Last name must bee more than 1 and less than 201 characters."),
    ], description="Enter your last name")

    first_name = StringField('First name', [
        validators.DataRequired(),
        validators.Length(min=2, max=200, message="First name must bee more than 1 and less than 201 characters."),
    ], description="Enter your first name")

    password = PasswordField('Your password', [
        validators.DataRequired(),
        validators.Length(min=6, max=100, message="Password must bee more than 5 and less than 101 characters."),
        validators.EqualTo('password_confirmation', message="Passwords not match"),
    ])

    password_confirmation = PasswordField(
        'Confirm password',
        [validators.DataRequired()],
        description="Confirm your password"
    )

    # Company block
    company_name = StringField('Company name', [
        validators.DataRequired(),
        validators.Length(min=3, max=200, message="Company name must bee more than 2 and less than 201 characters."),
    ])

    company_address = StringField('Company address', [
        base.NotRequired(),
        validators.Length(min=5, max=200, message="Address must bee more than 6 and less than 201 characters."),
    ])

    company_phone = StringField('Company phone', [
        base.NotRequired(),
        validators.Length(min=7, max=30, message="Phone must bee more than 6 and less than 30 characters."),
    ])

    company_email = StringField('Company e-mail', [
        validators.DataRequired(),
        validators.Length(min=5, max=200, message="Email must bee more than 4 and less than 201 characters."),
        validators.Email(message="Company e-mail must be valid email address"),
    ])


class WorkerRegistration(Form):
    uuid = HiddenField('Auth key [hidden]', [
        base.ValidationChain(
            base.UUID(message="Invalid or not provided secret key."),
            base.Exists(
                Worker,
                column='auth_key',
                message="Secret key not found or expired. Make sure that you still have invitation to system."
            ),
        )
    ])

    username = StringField('Username', [
        base.Unique(User),
        validators.DataRequired(),
        validators.Length(min=6, max=200, message="Username must bee more than 5 and less than 201 characters."),
    ], description="Enter your username")

    password = PasswordField('Your password', [
        validators.DataRequired(),
        validators.EqualTo('password_confirmation', message="Passwords not match"),
        validators.Length(min=6, max=100, message="Password must bee more than 5 and less than 101 characters."),
    ])

    password_confirmation = PasswordField(
        'Confirm password',
        [validators.DataRequired()],
        description="Confirm your password"
    )
