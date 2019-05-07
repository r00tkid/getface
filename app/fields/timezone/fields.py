import pytz

from django.core.exceptions import ValidationError
from django.utils.encoding import force_text
from django.db import models
from django.utils import six

from .utils import is_pytz_instance


class TimeZoneField(models.Field):
    description = "A pytz timezone object"

    # NOTE: these defaults are excluded from migrations. If these are changed,
    #       existing migration files will need to be accomodated.
    CHOICES = [
        (pytz.timezone(tz), tz.replace('_', ' '))
        for tz in pytz.common_timezones
    ]
    MAX_LENGTH = 63

    def __init__(self, *args, **kwargs):
        # allow some use of positional args up until the args we customize
        # https://github.com/mfogel/django-timezone-field/issues/42
        # https://github.com/django/django/blob/1.11.11/django/db/models/fields/__init__.py#L145
        if len(args) > 3:
            raise ValueError('Cannot specify max_length by positional arg')

        kwargs.setdefault('choices', self.CHOICES)
        kwargs.setdefault('max_length', self.MAX_LENGTH)

        # Choices can be specified in two forms: either
        # [<pytz.timezone>, <str>] or [<str>, <str>]
        #
        # The [<pytz.timezone>, <str>] format is the one we actually
        # store the choices in memory because of
        # https://github.com/mfogel/django-timezone-field/issues/24
        #
        # The [<str>, <str>] format is supported because since django
        # can't deconstruct pytz.timezone objects, migration files must
        # use an alternate format. Representing the timezones as strings
        # is the obvious choice.
        choices = kwargs['choices']
        if isinstance(choices[0][0], (six.string_types, six.binary_type)):
            kwargs['choices'] = [(pytz.timezone(n1), n2) for n1, n2 in choices]

        super(TimeZoneField, self).__init__(*args, **kwargs)

    def validate(self, value, model_instance):
        if not is_pytz_instance(value):
            raise ValidationError("'%s' is not a pytz timezone object" % value)
        super(TimeZoneField, self).validate(value, model_instance)

    def deconstruct(self):
        name, path, args, kwargs = super(TimeZoneField, self).deconstruct()
        if kwargs['choices'] == self.CHOICES:
            del kwargs['choices']
        if kwargs['max_length'] == self.MAX_LENGTH:
            del kwargs['max_length']

        if 'choices' in kwargs:
            kwargs['choices'] = [(tz.zone, n) for tz, n in kwargs['choices']]

        return name, path, args, kwargs

    def get_internal_type(self):
        return 'CharField'

    def get_default(self):
        # allow defaults to be still specified as strings. Allows for easy
        # serialization into migration files
        value = super(TimeZoneField, self).get_default()
        return self._get_python_and_db_repr(value)[0]

    def from_db_value(self, value, *args):
        return self._get_python_and_db_repr(value)[0]

    def to_python(self, value):
        return self._get_python_and_db_repr(value)[0]

    def get_prep_value(self, value):
        return self._get_python_and_db_repr(value)[1]

    def _get_python_and_db_repr(self, value):
        if value is None or value == '':
            return None, ''
        if is_pytz_instance(value):
            return value, value.zone
        try:
            return pytz.timezone(force_text(value)), force_text(value)
        except pytz.UnknownTimeZoneError:
            pass
        raise ValidationError("Invalid timezone '%s'" % value)
