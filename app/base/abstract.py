import datetime
from django.db import models


class TimeStumpModel(models.Model):
    created_at = models.DateTimeField('Date post created', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('Date post updated', auto_now=True, null=True)

    class Meta:
        abstract = True

    def to_serialize(self, take):
        return {key: self.__dict__[key] for key in take if key in self.__dict__}


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
