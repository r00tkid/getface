from index.base.repository import Base


class Create(Base.Validator):
    field = Base.Validator.field
    valid = Base.Validator.valid

    name = field.String("Company name", [
        valid.DataRequired(),
        valid.Length(
            min=6,
            max=200,
            message="Company name length must be between 6 and 200 characters inclusive."
        ),
    ], description="Name of company")

    description = field.TextArea("Company description", [
        valid.NotRequired(),
        valid.Length(
            min=10,
            max=4000,
            message="Company description length must be between 10 and 4000 characters inclusive."
        ),
    ], description="Name of company")

    address = field.String("Company address", [
        valid.NotRequired(),
        valid.Length(
            min=10,
            max=200,
            message="Company address length must be between 10 and 200 characters inclusive."
        ),
    ], description="Name of company")

    phone = field.String("Company phone", [
        valid.NotRequired(),
        valid.Length(min=6, max=30, message="Company phone length must be between 6 and 30 characters inclusive."),
    ], description="Name of company")

    email = field.String("Company email", [
        valid.DataRequired(),
        valid.Length(min=6, max=200, message="E-mail length must be between 6 and 200 characters inclusive."),
        valid.Email(message="E-mail must be valid email address"),
    ], description="Name of company")


class Update(Base.Validator):
    field = Base.Validator.field
    valid = Base.Validator.valid

    name = field.String("Company name", [
        valid.NotRequired(allow_empty=False),
        valid.Length(
            min=6,
            max=200,
            message="Company name length must be between 6 and 200 characters inclusive."
        ),
    ], description="Name of company")

    description = field.TextArea("Company description", [
        valid.NotRequired(),
        valid.Length(
            min=10,
            max=4000,
            message="Company description length must be between 10 and 4000 characters inclusive."
        ),
    ], description="Name of company")

    address = field.String("Company address", [
        valid.NotRequired(),
        valid.Length(
            min=10,
            max=200,
            message="Company address length must be between 10 and 200 characters inclusive."
        ),
    ], description="Name of company")

    phone = field.String("Company phone", [
        valid.NotRequired(),
        valid.Length(min=6, max=30, message="Company phone length must be between 6 and 30 characters inclusive."),
    ], description="Name of company")

    email = field.String("Company email", [
        valid.NotRequired(allow_empty=False),
        valid.Length(min=6, max=200, message="E-mail length must be between 6 and 200 characters inclusive."),
        valid.Email(message="E-mail must be valid email address"),
    ], description="Name of company")
