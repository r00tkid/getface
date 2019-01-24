from index.base.repository import Base


class Create(Base.Validator):
    field = Base.Validator.field
    valid = Base.Validator.valid

    name = field.String("Feature name", [
        valid.DataRequired(),
        valid.Length(min=5, max=256),
    ])

    description = field.TextArea("Feature description", [
        valid.DataRequired(),
        valid.Length(min=10, max=5000),
    ])

    link = field.String("Feature link [optional]", [
        valid.NotRequired(),
        valid.Length(max=1024),
    ])

    is_alive = field.Boolean("Display feature to user", [
        valid.NotRequired(is_string=False),
    ])

    is_important = field.Boolean("Important feature", [
        valid.NotRequired(is_string=False),
    ])


class Update(Base.Validator):
    field = Base.Validator.field
    valid = Base.Validator.valid

    name = field.String("Feature name", [
        valid.NotRequired(allow_empty=False),
        valid.Length(min=5, max=256),
    ])

    description = field.TextArea("Feature description", [
        valid.NotRequired(allow_empty=False),
        valid.Length(min=10, max=5000),
    ])

    link = field.String("Feature link [optional]", [
        valid.NotRequired(),
        valid.Length(max=1024),
    ])

    is_alive = field.Boolean("Display feature to user", [
        valid.NotRequired(is_string=False),
    ])

    is_important = field.Boolean("Important feature", [
        valid.NotRequired(is_string=False),
    ])
