from index.base.repository import Base
from company.models.company.model import Company


class Create(Base.Validator):
    field = Base.Validator.field
    valid = Base.Validator.valid

    name = field.String('Title', [
        valid.DataRequired(),
        valid.Length(min=2, max=200, message="Last name length must be between 2 and 200 characters inclusive."),
    ], description="Enter department name")

    company_id = field.Integer('Company ID', [
        valid.DataRequired(),
        valid.Exists(
            Company, 'id'
        ),
    ])


class Update(Create):
    pass
