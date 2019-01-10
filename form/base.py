from wtforms import ValidationError
import datetime, uuid
from dateutil import parser


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
        data = field.raw_data if field.raw_data else field.data

        if self.column.__eq__(None):
            self.column = field.name

        try:
            self.model.objects.get(**{self.column: data})
        except:
            # this means that this one not exist
            return

        raise ValidationError(self.message if self.message else "This field not unique")


class Exists(object):
    field_flags = ('exists',)

    def __init__(self, model, column=None, message=None):
        self.model = model
        self.column = column
        self.message = message

    def __call__(self, form, field):
        data = field.raw_data if field.raw_data else field.data

        if self.column.__eq__(None):
            self.column = field.name

        try:
            self.model.objects.get(**{self.column: data})
        except:
            raise ValidationError(self.message if self.message else "Given data doesn't exist")


class ValidationChain(object):
    field_flags = ('validation_chain',)

    def __init__(self, *validators):
        self.validators = validators

    def __call__(self, form, field):
        for validator in self.validators:
            validator(form, field)


class Expiration(object):
    field_flags = ('expiration',)

    def __init__(self, model=None, column=None, expiration=None, now=None, message=None):
        self.model = model
        self.column = column
        self.message = message

        if type(expiration).__name__ == 'str':
            self.expiration = parser.parse(expiration)
        elif type(now).__name__ == 'datetime':
            self.expiration = expiration

        if not now:
            self.now = datetime.datetime.now()
        else:
            if type(now).__name__ == 'str':
                self.now = parser.parse(now)
            elif type(now).__name__ == 'datetime':
                self.now = now
            else:
                raise TypeError("Unexpected [now] type")

    def __call__(self, form, field):
        data = field.raw_data if field.raw_data else field.data

        if self.model:
            try:
                model = self.model.objects.get(**{self.column: data})
            except:
                raise ValidationError("No model found")

            if model[self.column].__eq__(None):
                raise ValidationError("None not a date")

            if self.now > parser.parse(model[self.column]):
                raise ValidationError(self.message if self.message else "Has been expired")
            return

        if self.expiration:
            if self.now > self.expiration:
                raise ValidationError(self.message if self.message else "Has been expired")
            return

        try:
            if self.now > parser.parse(data):
                raise ValidationError(self.message if self.message else "Has been expired")
        except:
            raise ValidationError("Invalid [%s] field data" % field.name)


class UUID(object):
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        message = self.message

        if message is None:
            message = field.gettext('Invalid UUID.')
        try:
            uuid.UUID(field.data)
        except:
            raise ValidationError(message)


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
