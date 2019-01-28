from django.db import models
from index.base.query import SoftDeletionQuerySet


class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        self.dead_only = kwargs.pop('dead_only', False)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.dead_only:
            return SoftDeletionQuerySet(self.model).exclude(deleted_at=None)

        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(deleted_at=None)

        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()
