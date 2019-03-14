from index.base.repository import Base


class FeatureCreateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    name = field.String("Feature name", [
        validation.DataRequired(),
        validation.Length(min=5, max=256),
    ])

    description = field.TextArea("Feature description", [
        validation.DataRequired(),
        validation.Length(min=10, max=5000),
    ])

    link = field.String("Feature link [optional]", [
        validation.NotRequired(),
        validation.Length(max=1024),
    ])

    is_alive = field.Boolean("Display feature to user", [
        validation.NotRequired(is_string=False),
    ])

    is_important = field.Boolean("Important feature", [
        validation.NotRequired(is_string=False),
    ])


class FeatureUpdateValidator(Base.Validator):
    validation = Base.Validator.validation
    field = Base.Validator.field

    name = field.String("Feature name", [
        validation.NotRequired(allow_empty=False),
        validation.Length(min=5, max=256),
    ])

    description = field.TextArea("Feature description", [
        validation.NotRequired(allow_empty=False),
        validation.Length(min=10, max=5000),
    ])

    link = field.String("Feature link [optional]", [
        validation.NotRequired(),
        validation.Length(max=1024),
    ])

    is_alive = field.Boolean("Display feature to user", [
        validation.NotRequired(is_string=False),
    ])

    is_important = field.Boolean("Important feature", [
        validation.NotRequired(is_string=False),
    ])
