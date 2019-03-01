from typing import Type, Optional, Dict
from wtforms import Form
from rest_framework import serializers
from django.db import models
from django.contrib import admin

from index.base.exceptions import APIException
from index import settings


class Base(object):
    from index.base.model import CreatedStump, UpdatedStump, TimeStumps, SoftDeletion

    class Model(models.Model):
        from index.base import field
        from index.base import relations as rel

        def update(self, data, nullable=True):
            if nullable:
                [self.__setattr__(k, v) for k, v in data.items()]
            else:
                [self.__setattr__(k, v) for k, v in data.items() if v is not None]

            self.save(force_update=True)

        class Meta:
            abstract = True

    class Validator(Form):
        from index.base import formfield as field
        from index.base import validation as valid

    class Serializer(serializers.ModelSerializer):
        from rest_framework import serializers

    class ListSerializer(serializers.ListSerializer):
        pass

    class Admin(admin.ModelAdmin):
        from django.utils.html import format_html

    @classmethod
    def model(cls) -> Type[Model]:
        raise NotImplementedError

    @classmethod
    def admin_view(cls) -> Type[Admin]:
        raise NotImplementedError

    @classmethod
    def actions(cls) -> Dict[str, Type[Form]]:
        raise NotImplementedError

    @classmethod
    def serializers(cls) -> Dict[str, Type[Serializer]]:
        raise NotImplementedError

    @classmethod
    def action(cls, name: str = 'create') -> Type[Form]:
        return cls.actions()[name]

    @classmethod
    def serializer(cls, name: str = 'base') -> Type[Serializer]:
        return cls.serializers()[name]

    @classmethod
    def new(cls, data: dict) -> Model:
        """
        Don't use this method directly, until some special reasons.

        @param data: Data for user creation.
        @type data: dict
        """
        return cls.model()(**data)

    @classmethod
    def info(cls, pk, name: str = 'base', api_exception: bool = True) -> Optional[Serializer]:
        obj = cls.model().objects

        try:
            model = obj.get(pk=pk)
        except Exception as e:
            if api_exception:
                raise APIException({
                    'detail': '%(model)s id:[%(id)d] has not been found.' % {
                        'model': cls.model()._meta.verbose_name.title(),
                        'id': pk
                    },
                    'debug': str(e) if settings.DEBUG else None,
                }, 404)
            else:
                return None

        return cls.serializer(name)(instance=model)
