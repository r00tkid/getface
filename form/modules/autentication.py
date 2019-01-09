from wtforms import Form, StringField, PasswordField, validators
from form.base import NotRequired, Unique
from authentication.serializers import User


class Registration(Form):
    # Owner block
    username = StringField('Username', [
        Unique(User),
        validators.DataRequired(),
        validators.Length(min=6, max=200, message="Username must bee more than 5 and less than 201 characters."),
    ], description="Enter your username")

    email = StringField('E-mail', [
        validators.DataRequired(),
        validators.Length(min=5, max=200, message="E-mail must bee more than 4 and less than 201 characters."),
        validators.Email(message="E-mail must be valid email address"),
        Unique(User, message="E-mail not unique")
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
        NotRequired(),
        validators.Length(min=5, max=200, message="Address must bee more than 6 and less than 201 characters."),
    ])

    company_phone = StringField('Company phone', [
        NotRequired(),
        validators.Length(min=7, max=30, message="Phone must bee more than 6 and less than 30 characters."),
    ])

    company_email = StringField('Company e-mail', [
        validators.DataRequired(),
        validators.Length(min=5, max=200, message="Email must bee more than 4 and less than 201 characters."),
        validators.Email(message="Company e-mail must be valid email address"),
    ])
