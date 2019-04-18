from rest_framework.serializers import ModelSerializer as _Serializer, ListSerializer as _List
from rest_framework.serializers import SerializerMethodField as _Method


class CompanySerializer(_Serializer):
    class Meta:
        from holding.models.company.model import Company as _Company

        model = _Company
        fields = ('id', 'name', 'description', 'address', 'email', 'phone')


class CompanyExtendedListSerializer(_List):
    def add_owner(self):
        from holding.models import EmployeeSerializer

        for data, instance in zip(self.data, self.instance):
            data['owner'] = EmployeeSerializer(instance=instance.owner).data

        return self

    def add_rights(self, user):
        from holding.models import Employee, EmployeeSerializer

        for data, instance in zip(self.data, self.instance):
            employee = Employee.objects.filter(user=user, company=instance).first()

            data['as_employee'] = EmployeeSerializer(instance=employee).data

            if employee:
                data['rights'] = {}
                data['rights']['is_owner'] = instance.owner_id == employee.id
                data['rights']['is_manager'] = employee.is_manager or data['rights']['is_owner']
            else:
                data['rights'] = {
                    'is_owner': False,
                    'is_manager': False,
                }

            if not data['rights']['is_owner']:
                data['time_left'] = 0

        return self

    def add_employees(self):
        from holding.models import Employee, EmployeeSerializer

        for data, instance in zip(self.data, self.instance):
            data['employees'] = EmployeeSerializer(
                instance=Employee.objects.filter(company_id=instance.pk),
                many=True,
            ).data

        return self


class CompanyExtendedSerializer(_Serializer):
    time_zone = _Method()

    def get_time_zone(self, model):
        return model.timezone.zone

    def add_rights(self, user):
        from holding.models import Employee

        employee = Employee.objects.filter(user=user, company=self.instance).first()

        if employee:
            self.data['rights'] = {
                'is_owner': self.instance.owner_id == employee.id,
                'is_manager': employee.is_manager or self.instance.owner_id == employee.id,
            }
        else:
            self.data['rights'] = {
                'is_owner': False,
                'is_manager': False,
            }

        return self

    def add_owner(self):
        from holding.models import EmployeeSerializer

        self.data['owner'] = EmployeeSerializer(instance=self.instance.owner).data

    def add_employees(self):
        from holding.models import Employee, EmployeeSerializer

        employees = Employee.objects.filter(company_id=self.instance.pk)

        self.data['employees'] = EmployeeSerializer(instance=employees, many=True).data

    class Meta:
        from holding.models.company.model import Company as _Company

        model = _Company
        fields = ('id', 'name', 'description', 'address', 'email', 'phone', 'time_zone', 'time_left')
        list_serializer_class = CompanyExtendedListSerializer
