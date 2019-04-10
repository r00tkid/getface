# Getters
from app.base.helpers import get_model as __get
from . import User, Feature


@__get(model=User)
def get_user(id, raise_exception=True, obj=None) -> User:
    return obj


@__get(model=Feature)
def get_feature(id, raise_exception=True, obj=None) -> Feature:
    return obj
