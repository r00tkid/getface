from wtforms import Form, StringField, validators
from tech import base


class CreateWorker(Form):
    last_name = StringField('Last name', [
        validators.DataRequired(),
        validators.Length(min=2, max=200, message="Last name length must be between 2 and 200 characters inclusive."),
    ], description="Enter your last name")

    first_name = StringField('First name', [
        validators.DataRequired(),
        validators.Length(min=2, max=200, message="First name length must be between 2 and 200 characters inclusive."),
    ], description="Enter your first name")

    email = StringField('E-mail', [
        validators.DataRequired(),
        validators.Length(min=6, max=200, message="E-mail length must be between 6 and 200 characters inclusive."),
        validators.Email(message="E-mail must be valid email address"),
    ])

    phone = StringField('Phone', [
        base.NotRequired(),
        validators.Length(min=6, max=30, message="Phone length must be between 6 and 30 characters inclusive."),
    ])


class UpdateWorker(Form):
    last_name = StringField('Last name', [
        base.NotRequired(allow_empty=False),
        validators.Length(min=2, max=200, message="Last name length must be between 2 and 200 characters inclusive."),
    ], description="Enter your last name")

    first_name = StringField('First name', [
        base.NotRequired(allow_empty=False),
        validators.Length(min=2, max=200, message="First name length must be between 2 and 200 characters inclusive."),
    ], description="Enter your first name")

    email = StringField('E-mail', [
        base.NotRequired(),
        validators.Length(min=6, max=200, message="E-mail length must be between 6 and 200 characters inclusive."),
        validators.Email(message="E-mail must be valid email address"),
    ])

    phone = StringField('Phone', [
        base.NotRequired(),
        validators.Length(min=6, max=30, message="Phone length must be between 6 and 30 characters inclusive."),
    ])
