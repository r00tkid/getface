from index.base.repository import Base


class FeatureCreateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    name = field.string("Feature name", [
        validation.data_required(),
        validation.length(min=5, max=256),
    ])

    description = field.text_area("Feature description", [
        validation.data_required(),
        validation.length(min=10, max=5000),
    ])

    link = field.string("Feature link [optional]", [
        validation.not_required(),
        validation.length(max=1024),
    ])

    is_alive = field.boolean("Display feature to user", [
        validation.not_required(is_string=False),
    ])

    is_important = field.boolean("Important feature", [
        validation.not_required(is_string=False),
    ])


class FeatureUpdateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    name = field.string("Feature name", [
        validation.not_required(allow_empty=False),
        validation.length(min=5, max=256),
    ])

    description = field.text_area("Feature description", [
        validation.not_required(allow_empty=False),
        validation.length(min=10, max=5000),
    ])

    link = field.string("Feature link [optional]", [
        validation.not_required(),
        validation.length(max=1024),
    ])

    is_alive = field.boolean("Display feature to user", [
        validation.not_required(is_string=False),
    ])

    is_important = field.boolean("Important feature", [
        validation.not_required(is_string=False),
    ])
