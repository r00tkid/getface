from django.db.models import Model as _Model
import typing as _tp
import re as _r


def get_model(model: _Model):
    if not isinstance(model, _Model):
        raise AttributeError()

    def decorator(func: _tp.Callable):
        # Function signature must bee (model_id, raise_exception=True, model_obj=None)!

        def wrapper(model_id, raise_exception=True) -> _Model:
            from .exceptions import NotFound

            model_obj = model.objects.filter(pk=model_id).first()

            if not model_obj and raise_exception:
                raise NotFound()

            return func(model_id, raise_exception, model_obj)

        return wrapper

    return decorator


_first_cap = _r.compile('(.)([A-Z][a-z]+)')
_all_cap = _r.compile('([a-z0-9])([A-Z])')


def snake(string):
    string = _r.sub(_first_cap, r'\1_\2', string)
    return _r.sub(_all_cap, r'\1_\2', string).lower()


def camel(string):
    parts = string.split('_')

    if len(parts) == 1:
        return string.title()

    return "".join([part.title() for part in parts])
