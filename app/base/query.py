from django.db.models import QuerySet as __QuerySet


class SoftDeletionQuerySet(__QuerySet):
    def delete(self):
        from datetime import datetime

        return super(SoftDeletionQuerySet, self).update(deleted_at=datetime.now())

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        return self.filter(deleted_at=None)

    def dead(self):
        return self.exclude(deleted_at=None)
