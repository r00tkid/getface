from index.base.repository import Base


class CompanyCreateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    name = field.string("Company name", [
        validation.data_required(),
        validation.length(
            min=6,
            max=200,
            message="Company name length must be between 6 and 200 characters inclusive."
        ),
    ], description="Name of company")

    description = field.text_area("Company description", [
        validation.not_required(),
        validation.length(
            min=10,
            max=4000,
            message="Company description length must be between 10 and 4000 characters inclusive."
        ),
    ], description="Name of company")

    address = field.string("Company address", [
        validation.not_required(),
        validation.length(
            min=10,
            max=200,
            message="Company address length must be between 10 and 200 characters inclusive."
        ),
    ], description="Name of company")

    phone = field.string("Company phone", [
        validation.not_required(),
        validation.length(min=6, max=30, message="Company phone length must be between 6 and 30 characters inclusive."),
    ], description="Name of company")

    email = field.string("Company email", [
        validation.data_required(),
        validation.length(min=6, max=200, message="E-mail length must be between 6 and 200 characters inclusive."),
        validation.email(message="E-mail must be valid email address"),
    ], description="Name of company")


class CompanyUpdateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    name = field.string("Company name", [
        validation.not_required(allow_empty=False),
        validation.length(
            min=6,
            max=200,
            message="Company name length must be between 6 and 200 characters inclusive."
        ),
    ], description="Name of company")

    description = field.text_area("Company description", [
        validation.not_required(),
        validation.length(
            min=10,
            max=4000,
            message="Company description length must be between 10 and 4000 characters inclusive."
        ),
    ], description="Name of company")

    address = field.string("Company address", [
        validation.not_required(),
        validation.length(
            min=10,
            max=200,
            message="Company address length must be between 10 and 200 characters inclusive."
        ),
    ], description="Name of company")

    phone = field.string("Company phone", [
        validation.not_required(),
        validation.length(min=6, max=30, message="Company phone length must be between 6 and 30 characters inclusive."),
    ], description="Name of company")

    email = field.string("Company email", [
        validation.not_required(allow_empty=False),
        validation.length(min=6, max=200, message="E-mail length must be between 6 and 200 characters inclusive."),
        validation.email(message="E-mail must be valid email address"),
    ], description="Name of company")
