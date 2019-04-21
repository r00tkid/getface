class Validations:
    from wtforms.validators import (
        Email as __Email,
        DataRequired as __DataRequired,
        EqualTo as __EqualTo,
        IPAddress as __IPAddress,
        Length as __Length,
        Regexp as __Regexp,
        URL as __URL,
        AnyOf as __AnyOf,
        NoneOf as __NoneOf,
        MacAddress as __MacAddress,
    )

    class __NotRequired(object):
        field_flags = ('optional',)

        def __init__(self, strip_whitespace=True, is_string=True, allow_empty=True):
            self.is_string = is_string
            self.allow_empty = allow_empty

            if strip_whitespace:
                self.string_check = lambda s: s.strip()
            else:
                self.string_check = lambda s: s

        def __call__(self, form, field):
            from wtforms import validators, compat

            if self.is_string:
                if isinstance(field.data, str):
                    field.data = field.default

            if not self.allow_empty and field.data == "":
                field.data = None

            if not field.data or isinstance(field.data[0], compat.string_types) \
                    and not self.string_check(field.data[0]):
                field.errors[:] = []
                raise validators.StopValidation()

    class __Unique(object):
        field_flags = ('unique',)

        def __init__(self, model, column=None, message=None):
            self.model = model
            self.column = column
            self.message = message

        def __call__(self, form, field):
            from wtforms import ValidationError

            data = field.raw_data if field.raw_data else field.data

            if not self.column:
                self.column = field.name

            try:
                self.model.objects.get(**{self.column: data})
            except:
                # this means that this one not exist
                return

            raise ValidationError(self.message if self.message else "This field not unique")

    class __Exists(object):
        field_flags = ('exists',)

        def __init__(self, model, column=None, message=None):
            self.model = model
            self.column = column
            self.message = message

        def __call__(self, form, field):
            from wtforms import ValidationError

            data = field.raw_data if field.raw_data else field.data

            if not self.column:
                self.column = field.name

            try:
                self.model.objects.get(**{self.column: data})
            except Exception as e:
                raise ValidationError(self.message if self.message else "Given data doesn't exist")

    class __ValidationChain(object):
        field_flags = ('validation_chain',)

        def __init__(self, *validators):
            self.validators = validators

        def __call__(self, form, field):
            for validator in self.validators:
                validator(form, field)

    class __Expiration(object):
        field_flags = ('expiration',)

        def __init__(self, model=None, column=None, expiration=None, now=None, message=None):
            from datetime import datetime
            from dateutil import parser

            self.model = model
            self.column = column
            self.message = message

            def check_set(param, value):
                if isinstance(value, str):
                    setattr(self, param, parser.parse(value))
                elif isinstance(expiration, datetime):
                    setattr(self, param, value)

            check_set('expiration', expiration)

            if not now:
                self.now = datetime.now()
            else:
                check_set('now', now)

        def __call__(self, form, field):
            from wtforms import ValidationError
            from dateutil import parser

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

    class __UUID(object):
        def __init__(self, message=None):
            self.message = message

        def __call__(self, form, field):
            from uuid import UUID
            from wtforms import ValidationError

            message = self.message

            if message is None:
                message = field.gettext('Invalid UUID.')
            try:
                UUID(field.data)
            except:
                raise ValidationError(message)

    class __NumberRange(object):
        def __init__(self, min=None, max=None, message=None):
            self.min = min
            self.max = max
            self.message = message

        def __call__(self, form, field):
            from wtforms import ValidationError

            try:
                data = int(field.data)
            except:
                raise ValidationError("Field must be a number.")

            if data is None or (self.min is not None and data < self.min) or (self.max is not None and data > self.max):
                message = self.message
                if message is None:
                    if self.max is None:
                        message = field.gettext('Number must be at least %(min)s.')
                    elif self.min is None:
                        message = field.gettext('Number must be at most %(max)s.')
                    else:
                        message = field.gettext('Number must be between %(min)s and %(max)s.')

                raise ValidationError(message % dict(min=self.min, max=self.max))

    validation_chain = __ValidationChain
    data_required = __DataRequired
    not_required = __NotRequired
    number_range = __NumberRange
    mac_address = __MacAddress
    expiration = __Expiration
    ip_address = __IPAddress
    equal_to = __EqualTo
    none_of = __NoneOf
    length = __Length
    unique = __Unique
    exists = __Exists
    regexp = __Regexp
    any_of = __AnyOf
    email = __Email
    uuid = __UUID
    url = __URL
