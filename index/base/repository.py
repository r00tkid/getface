class Base(object):
    from wtforms import Form as __Form

    from django.contrib import admin
    from rest_framework import serializers

    class models:
        from index.base.model import CreatedStump, UpdatedStump, TimeStumps, SoftDeletion, Model

    class Validator(__Form):
        from index.base.formfields import FormFields as __FormFields
        from index.base.validations import Validations as __Validations

        field = __FormFields
        validation = __Validations

    class Serializer(serializers.ModelSerializer):
        pass

    class ListSerializer(serializers.ListSerializer):
        pass

    class Admin(admin.ModelAdmin):
        from django.utils.html import format_html
