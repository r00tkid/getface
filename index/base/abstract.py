import datetime
from django.db import models


class Model(models.Model):
    class Meta:
        abstract = True

    def update(self, data, nullable=True, using=None, update_fields=None):
        """
        Definitely updates your model

        Update args:
            @param data: Model data to update
            @type data: dict
            @param nullable: Is fields can be nullable
            @type nullable: bool

        Save args:
            @param using: DB for write
            @type using: (None) -> str
            @param update_fields: Fields that going to be updated
            @type update_fields: (None, set, frozenset, list, tuple) -> frozenset
        """
        return self.fill(
            data,
            nullable
        ).save(
            force_update=True,
            update_fields=update_fields,
            using=using,
        )

    def fill(self, data, nullable=True):
        if nullable:
            [self.__setattr__(k, v) for k, v in data.items()]
        else:
            [self.__setattr__(k, v) for k, v in data.items() if v is not None]

        return self

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        return self


class TimeStumpModel(Model):
    created_at = models.DateTimeField('Date record created', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('Date record updated', auto_now=True, null=True)

    class Meta:
        abstract = True


class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(deleted_at=None)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()


class SoftDeletionQuerySet(models.QuerySet):
    def delete(self):
        return super(SoftDeletionQuerySet, self).update(deleted_at=datetime.datetime.now())

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        return self.filter(deleted_at=None)

    def dead(self):
        return self.exclude(deleted_at=None)


class SoftDeletesModel(TimeStumpModel):
    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    # Deleted at field
    deleted_at = models.DateTimeField(
        editable=False,
        blank=True,
        null=True,
    )

    def delete(self, **kwargs):
        self.deleted_at = datetime.datetime.now()
        self.save()

    def hard_delete(self):
        super(SoftDeletesModel, self).delete()

    class Meta:
        abstract = True
