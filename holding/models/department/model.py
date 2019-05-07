from app.base.model import Model as _Model
from app.base.exceptions import APIException as _APIException


class Department(_Model):
    from django.db.models import fields as _field
    from django.db.models.fields import related as _related
    from django.db.models import deletion as _deletion

    name = _field.CharField(
        verbose_name='Название отдела',
        max_length=255,
        null=False,
        blank=False,
    )

    company = _related.ForeignKey(
        'holding.Company',
        verbose_name='Компания',
        on_delete=_deletion.SET_NULL,
        null=True,
        blank=True,
        related_name="departments",
    )

    is_protected = _field.BooleanField(
        verbose_name='Неудаляемый отдел',
        default=False,
    )

    @property
    def employee_amount(self):
        return self.employees.count()

    employee_amount.fget.short_description = "Кол-во сотрудников"

    def __str__(self):
        return self.name

    def delete(self, **kwargs):
        if self.is_protected:
            raise _APIException({
                'detail': 'Protected',
                'protected': True,
            }, status_code=403)

        super(Department, self).delete(**kwargs)

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"

    def attach_position(self, position):
        from holding.models import PositionToDepartment

        position.save()

        old_connection = PositionToDepartment.objects.filter(position_id=position.id, department_id=self.id).first()

        if old_connection:
            old_connection.save(department=self)
        else:
            PositionToDepartment(department=self, position=position).save()

        return self

    def create_position(self, name, **kwargs):
        from holding.models import Position

        if not self.id:
            self.save()

        position = Position(
            name=name,
            company=kwargs.get('company') if kwargs.get('company') else self.company,
            is_protected=kwargs.get('is_protected', False),
        )

        self.attach_position(position)

        return position
