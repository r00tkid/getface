from index.base.repository import Base


class DiscountCreateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    name = field.string('Name', [
        validation.data_required(),
        validation.length(min=2, max=200),
    ], description="Enter discount name")

    percent = field.integer('Discount in percents [0-100]', [
        validation.data_required(),
        validation.length(min=0, max=100),
    ], description="Enter discount rate")
