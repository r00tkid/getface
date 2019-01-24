from datetime import datetime
from django.db.models import Model
from index.base import field


class CreatedStump(Model):
    created_at = field.DateTime('Date record created', auto_now_add=True, null=True)

    class Meta:
        abstract = True


class UpdatedStump(Model):
    updated_at = field.DateTime('Date record updated', auto_now=True, null=True)

    class Meta:
        abstract = True


class TimeStumps(CreatedStump, UpdatedStump):
    class Meta:
        abstract = True


class SoftDeletion(Model):
    from index.base.manager import SoftDeletionManager

    manager = SoftDeletionManager
    objects = manager()
    deleted = manager(dead_only=True)
    all = manager(alive_only=False)

    # Deleted at field
    deleted_at = field.DateTime(
        editable=False,
        blank=True,
        null=True,
    )

    def delete(self, **kwargs):
        self.deleted_at = datetime.now()
        self.save()

    def hard_delete(self):
        super(SoftDeletion, self).delete()

    def update(self, data, nullable=True):
        if nullable:
            [self.__setattr__(k, v) for k, v in data.items()]
        else:
            [self.__setattr__(k, v) for k, v in data.items() if v is not None]

        self.save()

    class Meta:
        abstract = True
