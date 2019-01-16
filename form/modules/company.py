from wtforms import Form, StringField, TextField, validators
from form import base


class RegisterCompany(Form):
    name = StringField("Company name", [
        validators.DataRequired(),
        validators.Length(
            min=6,
            max=200,
            message="Company name length must be between 6 and 200 characters inclusive."
        ),
    ], description="Name of company")

    description = TextField("Company description", [
        base.NotRequired(),
        validators.Length(
            min=10,
            max=4000,
            message="Company description length must be between 10 and 4000 characters inclusive."
        ),
    ], description="Name of company")

    address = StringField("Company address", [
        base.NotRequired(),
        validators.Length(
            min=10,
            max=200,
            message="Company address length must be between 10 and 200 characters inclusive."
        ),
    ], description="Name of company")

    phone = StringField("Company phone", [
        base.NotRequired(),
        validators.Length(min=6, max=30, message="Company phone length must be between 6 and 30 characters inclusive."),
    ], description="Name of company")

    email = StringField("Company email", [
        validators.DataRequired(),
        validators.Length(min=6, max=200, message="E-mail length must be between 6 and 200 characters inclusive."),
        validators.Email(message="E-mail must be valid email address"),
    ], description="Name of company")


class UpdateCompany(Form):
    name = StringField("Company name", [
        base.NotRequired(allow_empty=False),
        validators.Length(
            min=6,
            max=200,
            message="Company name length must be between 6 and 200 characters inclusive."
        ),
    ], description="Name of company")

    description = TextField("Company description", [
        base.NotRequired(),
        validators.Length(
            min=10,
            max=4000,
            message="Company description length must be between 10 and 4000 characters inclusive."
        ),
    ], description="Name of company")

    address = StringField("Company address", [
        base.NotRequired(),
        validators.Length(
            min=10,
            max=200,
            message="Company address length must be between 10 and 200 characters inclusive."
        ),
    ], description="Name of company")

    phone = StringField("Company phone", [
        base.NotRequired(),
        validators.Length(min=6, max=30, message="Company phone length must be between 6 and 30 characters inclusive."),
    ], description="Name of company")

    email = StringField("Company email", [
        base.NotRequired(allow_empty=False),
        validators.Length(min=6, max=200, message="E-mail length must be between 6 and 200 characters inclusive."),
        validators.Email(message="E-mail must be valid email address"),
    ], description="Name of company")
