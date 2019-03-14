from django.db.models import Model as __Model


class CreatedStump(__Model):
    from index.base.fields import Fields as __Fields
    from index.base.relations import Relations as __Relations

    field = __Fields
    relation = __Relations

    created_at = field.date_time('Date record created', auto_now_add=True, null=True)

    def update(self, data, nullable=True):
        if nullable:
            [self.__setattr__(k, v) for k, v in data.items()]
        else:
            [self.__setattr__(k, v) for k, v in data.items() if v is not None]

        self.save(force_update=True)

    class Meta:
        abstract = True


class UpdatedStump(__Model):
    from index.base.fields import Fields as __Fields
    from index.base.relations import Relations as __Relations

    field = __Fields
    relation = __Relations

    updated_at = field.date_time('Date record updated', auto_now=True, null=True)

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
    from index.base.fields import Fields as __Fields
    from index.base.relations import Relations as __Relations
    from index.base.manager import SoftDeletionManager

    field = __Fields
    relation = __Relations

    manager = SoftDeletionManager
    objects = manager()
    deleted = manager(dead_only=True)
    all = manager(alive_only=False)

    # Deleted at field
    deleted_at = field.date_time(
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
    class Meta:
        abstract = True
