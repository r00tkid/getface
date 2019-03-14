from django.db.models import Model as __Model


class CreatedStump(__Model):
    from index.base import field, relations  # do not remove

    created_at = field.DateTime('Date record created', auto_now_add=True, null=True)

    def update(self, data, nullable=True):
        if nullable:
            [self.__setattr__(k, v) for k, v in data.items()]
        else:
            [self.__setattr__(k, v) for k, v in data.items() if v is not None]

        self.save(force_update=True)

    class Meta:
        abstract = True


class UpdatedStump(__Model):
    from index.base import field, relations  # do not remove

    updated_at = field.DateTime('Date record updated', auto_now=True, null=True)

    def update(self, data, nullable=True):
        if nullable:
            [self.__setattr__(k, v) for k, v in data.items()]
        else:
            [self.__setattr__(k, v) for k, v in data.items() if v is not None]

        self.save(force_update=True)

    class Meta:
        abstract = True


class TimeStumps(CreatedStump, UpdatedStump):
    class Meta:
        abstract = True


class SoftDeletion(__Model):
    from index.base import field, relations  # do not remove
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
        from datetime import datetime

        self.deleted_at = datetime.now()
        self.save()

    def hard_delete(self):
        super(SoftDeletion, self).delete()

    def update(self, data, nullable=True):
        if nullable:
            [self.__setattr__(k, v) for k, v in data.items()]
        else:
            [self.__setattr__(k, v) for k, v in data.items() if v is not None]

        self.save(force_update=True)

    class Meta:
        abstract = True


class Model(TimeStumps, SoftDeletion):
    pass

    class Meta:
        abstract = True
