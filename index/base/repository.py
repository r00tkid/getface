from wtforms import Form
from rest_framework import serializers
from django.db import models
from django.contrib import admin


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
