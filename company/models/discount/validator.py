from index.base.repository import Base


class Create(Base.Validator):
    field = Base.Validator.field
    valid = Base.Validator.valid

    name = field.String('Name', [
        valid.DataRequired(),
        valid.Length(min=2, max=200),
    ], description="Enter discount name")

    percent = field.Integer('Discount in percents [0-100]', [
        valid.DataRequired(),
        valid.Length(min=0, max=100),
    ], description="Enter discount rate")
