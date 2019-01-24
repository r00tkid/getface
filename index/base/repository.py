from wtforms import Form
from rest_framework import serializers
from django.db import models
from django.contrib import admin

from index.base.exceptions import NotFound
from index import settings


class Base(object):
    from index.base.model import CreatedStump, UpdatedStump, TimeStumps, SoftDeletion

    class Model(models.Model):
        from index.base import field
        from index.base import relations as rel
        class Meta:
            abstract = True

    class Validator(Form):
        from index.base import formfield as field
        from index.base import validation as valid

    class Serializer(serializers.ModelSerializer):
        from rest_framework import serializers

    class Admin(admin.ModelAdmin):
        from django.utils.html import format_html

    @classmethod
    def model(cls):
        raise NotImplementedError

    @classmethod
    def admin_view(cls):
        raise NotImplementedError

    @classmethod
    def actions(cls):
        raise NotImplementedError

    @classmethod
    def serializers(cls):
        raise NotImplementedError

    @classmethod
    def action(cls, name):
        return cls.actions()[name]

    @classmethod
    def serializer(cls, name):
        return cls.serializers()[name]

    @classmethod
    def new(cls, data):
        """
        Don't use this method directly, until some special reasons.

        @param data: Data for user creation.
        @type data: dict
        """
        return cls.model()(**data)

    @classmethod
    def info(cls, pk, name=None, api_exception=True):
        obj = cls.model().objects

        try:
            model = obj.get(pk=pk)
        except Exception as e:
            if api_exception:
                raise NotFound({
                    'detail': '%(model)s id:[%(id)d] has not been found.' % {
                        'model': type(cls.model()).__name__,
                        'id': pk
                    },
                    'debug': str(e) if settings.DEBUG else None,
                })
            else:
                return None

        return cls.serializer(name=name if name else 'base')(instance=model)
