class NotRequired(object):
    field_flags = ('optional',)

    def __init__(self, strip_whitespace=True, is_string=True):
        self.is_string = is_string

        if strip_whitespace:
            self.string_check = lambda s: s.strip()
        else:
            self.string_check = lambda s: s

    def __call__(self, form, field):
        from wtforms import validators, compat
        if self.is_string:
            if 'str' != type(field.data).__name__:
                field.data = field.default

        if not field.data or isinstance(field.data[0], compat.string_types) \
                and not self.string_check(field.data[0]):
            field.errors[:] = []
            raise validators.StopValidation()


class Unique(object):
    field_flags = ('unique',)

    def __init__(self, model, column=None, message=None):
        self.model = model
        self.column = column
        self.message = message

    def __call__(self, form, field):
        from wtforms import ValidationError
        data = field.raw_data if field.raw_data else field.data

        if self.column.__eq__(None):
            self.column = field.name

        try:
            self.model.objects.get(**{self.column: data})
        except:
            # this means that this one not exist
            return

        raise ValidationError(self.message if self.message else "This field not unique")


def fields_dictionary(name):
    return {
        'StringField': 'text',
        'PasswordField': 'password',
        'BooleanField': 'radio',
        'FileField': 'file',
        'DecimalField': 'number',
        'IntegerField': 'number',
        'FloatField': 'number',
        'DateField': 'date',
        'TimeField': 'time',
        'DateTimeField': 'datetime-local',
    }.get(name, 'text')


def get_form_fields(form):
    try:
        name = form.name
    except:
        name = type(form).__name__

    return {
        'form': name,
        'fields': [{
            'name': field.name,
            'label': field.label.text,
            'description': field.description,
            'type': fields_dictionary(field.type),
            'original_type': field.type,
            'default': field.default,
            'required': field.flags.required,
        } for field in form]
    }
