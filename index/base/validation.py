from functools import partial
from index.base.exceptions import UnprocessableEntityException


class Validations(object):
    @staticmethod
    def max(data, maximum):
        maximum = int(maximum)

        if 'int' == type(data).__name__:
            return "Field must be lower than %s." % maximum if data > maximum else True

        return "Field must contain %s characters or lower." % maximum if str(data).__len__() > maximum else True

    @staticmethod
    def min(data, minimum):
        minimum = int(minimum)

        if 'int' == type(data).__name__:
            return "Field must be more than %s." % minimum if data < minimum else True

        return "Field must contain %s characters or more." % minimum if str(data).__len__() < minimum else True


class StandAloneValidator(object):
    def __init__(self, o, validations, messages=None):
        """
        @type o: Union[object, dict]
        @type validations: dict
        """
        self.object = o
        self.validators = {}
        self.validations = {}
        self.errors = {}
        self.data = {}
        self.messages = messages
        self.prepare_validations(validations)

    def prepare_validations(self, validations):
        for field, validation in validations.items():
            if field not in self.validations.keys():
                self.validations[field] = {}

            if 'str' == type(validation).__name__:
                temp = [v.strip() for v in validation.split('|')]

                for v in temp:
                    if ":" in v:
                        v = v.split(":")
                        self.validations[field].__setitem__(v[0], v[1])
                    else:
                        self.validations[field].__setitem__(v, None)

            elif 'dict' == type(validation).__name__:
                self.validations[field].update(validation)
            else:
                raise Exception("Validation inner can only be type of str or dict.")

    def add_validator(self, name, callback):
        self.validators[name] = callback

    def __validation(self, field, data, validator_name, validator, *args):
        if args:
            result = validator(data, *args)
        else:
            result = validator(data)

        if 'str' == type(result).__name__:
            if not self.errors.get(field):
                self.errors[field] = []

            if self.messages and self.messages.get(field) and self.messages.get(field).get(validator_name):
                self.errors[field].append(self.messages.get(field).get(validator_name))
            else:
                self.errors[field].append(result)
        elif False is result:
            return result

    def validate(self, throw_exception=False, message=None):
        for field, validators in self.validations.items():
            for val_name, args in validators.items():
                val_call = getattr(Validations, val_name) if not self.validators.get(
                    val_name
                ) else self.validators.get(val_name)

                if 'dict' == type(self.object).__name__:
                    validation = partial(
                        self.__validation,
                        field,
                        self.object.get(field),
                        val_name,
                        val_call
                    )
                else:
                    validation = partial(
                        self.__validation,
                        field,
                        getattr(self.object, field),
                        val_name,
                        val_call
                    )

                if validation(args) is not None:
                    break

        if len(self.errors) > 0 and throw_exception:
            raise UnprocessableEntityException({
                'detail': message if message else 'Validation failed.',
                'errors': self.errors,
                'computed': {k: " ".join(v) for k, v in self.errors.items()},
            })
