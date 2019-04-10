from django.db.models import Model as _Model
import typing as _tp


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
