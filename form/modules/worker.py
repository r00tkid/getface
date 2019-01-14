from wtforms import Form, StringField, PasswordField, HiddenField, validators
from form import base
from authentication.serializers import User
from company.models import Worker


class CreateWorker(Form):
    last_name = StringField('Last name', [
        validators.DataRequired(),
        validators.Length(min=2, max=200, message="Last name must bee more than 1 and less than 201 characters."),
    ], description="Enter your last name")

    first_name = StringField('First name', [
        validators.DataRequired(),
        validators.Length(min=2, max=200, message="First name must bee more than 1 and less than 201 characters."),
    ], description="Enter your first name")

    email = StringField('E-mail', [
        validators.DataRequired(),
        validators.Length(min=6, max=200, message="E-mail must bee more than 6 and less than 201 characters."),
        validators.Email(message="E-mail must be valid email address"),
    ])


class UpdateWorker(Form):
    pass
