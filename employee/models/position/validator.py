from index.base.repository import Base
from company.models.company.model import Company


class PositionCreateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    name = field.string('Title', [
        validation.data_required(),
        validation.length(min=2, max=200, message="Last name length must be between 2 and 200 characters inclusive."),
    ], description="Enter department name")

    company_id = field.integer('Company ID', [
        validation.data_required(),
        validation.exists(
            Company, 'id'
        ),
    ])


class PositionUpdateValidator(PositionCreateValidator):
    pass
