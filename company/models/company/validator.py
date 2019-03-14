from index.base.repository import Base


class CompanyCreateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    name = field.String("Company name", [
        validation.DataRequired(),
        validation.Length(
            min=6,
            max=200,
            message="Company name length must be between 6 and 200 characters inclusive."
        ),
    ], description="Name of company")

    description = field.TextArea("Company description", [
        validation.NotRequired(),
        validation.Length(
            min=10,
            max=4000,
            message="Company description length must be between 10 and 4000 characters inclusive."
        ),
    ], description="Name of company")

    address = field.String("Company address", [
        validation.NotRequired(),
        validation.Length(
            min=10,
            max=200,
            message="Company address length must be between 10 and 200 characters inclusive."
        ),
    ], description="Name of company")

    phone = field.String("Company phone", [
        validation.NotRequired(),
        validation.Length(min=6, max=30, message="Company phone length must be between 6 and 30 characters inclusive."),
    ], description="Name of company")

    email = field.String("Company email", [
        validation.DataRequired(),
        validation.Length(min=6, max=200, message="E-mail length must be between 6 and 200 characters inclusive."),
        validation.Email(message="E-mail must be valid email address"),
    ], description="Name of company")


class CompanyUpdateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    name = field.String("Company name", [
        validation.NotRequired(allow_empty=False),
        validation.Length(
            min=6,
            max=200,
            message="Company name length must be between 6 and 200 characters inclusive."
        ),
    ], description="Name of company")

    description = field.TextArea("Company description", [
        validation.NotRequired(),
        validation.Length(
            min=10,
            max=4000,
            message="Company description length must be between 10 and 4000 characters inclusive."
        ),
    ], description="Name of company")

    address = field.String("Company address", [
        validation.NotRequired(),
        validation.Length(
            min=10,
            max=200,
            message="Company address length must be between 10 and 200 characters inclusive."
        ),
    ], description="Name of company")

    phone = field.String("Company phone", [
        validation.NotRequired(),
        validation.Length(min=6, max=30, message="Company phone length must be between 6 and 30 characters inclusive."),
    ], description="Name of company")

    email = field.String("Company email", [
        validation.NotRequired(allow_empty=False),
        validation.Length(min=6, max=200, message="E-mail length must be between 6 and 200 characters inclusive."),
        validation.Email(message="E-mail must be valid email address"),
    ], description="Name of company")
