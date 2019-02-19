from index.base.repository import Base
from authentication.models import User
from company.models.company.model import Company
from employee.models.employee.model import Employee
from employee.models.employee.serializer import BaseEmployee, ExtendedEmployee


def get_employee_serializer(name):
    return {
        'base': BaseEmployee,
        'extended': ExtendedEmployee,
    }[name]


class BaseCompany(Base.Serializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'address', 'email', 'phone')


class ExtendedCompanyList(Base.ListSerializer):
    def add_owner(self):
        for data, instance in zip(self.data, self.instance):
            data['owner'] = User.serializer()(instance=instance.owner).data

    def add_employee_info(self, user=None, field_name='employee'):
        for data, instance in zip(self.data, self.instance):
            if not user:
                data[field_name] = None
            else:
                data[field_name] = BaseEmployee(
                    instance=Employee.objects.filter(user=user, company=instance).first()
                ).data

    def add_employees(self, name='base'):
        for data, instance in zip(self.data, self.instance):
            serial = get_employee_serializer(name)

            data['employees'] = serial(
                instance=Employee.objects.filter(company_id=instance.pk),
                many=True,
            ).data

    def update(self, instance, validated_data):
        super().update(instance, validated_data)


class ExtendedCompany(Base.Serializer):
    def add_owner(self):
        self.data['owner'] = User.serializer()(instance=self.instance.owner).data

    def add_employees(self):
        employees = Employee.objects.filter(company_id=self.instance.pk)

        self.data['employees'] = BaseEmployee(instance=employees, many=True).data

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'address', 'email', 'phone')
        list_serializer_class = ExtendedCompanyList
