from index.base.repository import Base


class Create(Base.Validator):
    field = Base.Validator.field
    valid = Base.Validator.valid

    last_name = field.String('Last name', [
        valid.DataRequired(),
        valid.Length(min=2, max=200, message="Last name length must be between 2 and 200 characters inclusive."),
    ], description="Enter your last name")

    first_name = field.String('First name', [
        valid.DataRequired(),
        valid.Length(min=2, max=200, message="First name length must be between 2 and 200 characters inclusive."),
    ], description="Enter your first name")

    email = field.String('E-mail', [
        valid.DataRequired(),
        valid.Length(min=6, max=200, message="E-mail length must be between 6 and 200 characters inclusive."),
        valid.Email(message="E-mail must be valid email address"),
    ])

    phone = field.String('Phone', [
        valid.NotRequired(),
        valid.Length(min=6, max=30, message="Phone length must be between 6 and 30 characters inclusive."),
    ])


class Update(Base.Validator):
    field = Base.Validator.field
    valid = Base.Validator.valid

    last_name = field.String('Last name', [
        valid.NotRequired(allow_empty=False),
        valid.Length(min=2, max=200, message="Last name length must be between 2 and 200 characters inclusive."),
    ], description="Enter your last name")

    first_name = field.String('First name', [
        valid.NotRequired(allow_empty=False),
        valid.Length(min=2, max=200, message="First name length must be between 2 and 200 characters inclusive."),
    ], description="Enter your first name")

    email = field.String('E-mail', [
        valid.NotRequired(),
        valid.Length(min=6, max=200, message="E-mail length must be between 6 and 200 characters inclusive."),
        valid.Email(message="E-mail must be valid email address"),
    ])

    phone = field.String('Phone', [
        valid.NotRequired(),
        valid.Length(min=6, max=30, message="Phone length must be between 6 and 30 characters inclusive."),
    ])
