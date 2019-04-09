from rest_framework.serializers import ModelSerializer as _Serializer, ListSerializer as _List
from rest_framework.serializers import SerializerMethodField as _Method


class CompanySerializer(_Serializer):
    class Meta:
        from holding.models.company.model import Company as _Company

        model = _Company
        fields = ('id', 'name', 'description', 'address', 'email', 'phone')


class CompanyExtendedListSerializer(_List):
    from holding.models.employee.serializers import EmployeeSerializer as _SEmployee
    from holding.models.employee.model import Employee as _Employee

    def add_owner(self):
        for data, instance in zip(self.data, self.instance):
            data['owner'] = self._SEmployee(instance=instance.owner).data

        return self

    def add_rights(self, user, add_employee_info=False):
        for data, instance in zip(self.data, self.instance):
            employee = self._Employee.objects.filter(user=user, company=instance).first()

            data['as_employee'] = self._SEmployee(
                instance=self._Employee.objects.filter(user=user, company=instance).first()
            ).data if employee and add_employee_info else None

            data['rights'] = {
                'is_owner': instance.owner_id == user.id,
                'is_manager': employee.is_manager if employee else False or instance.owner_id == user.id,
            }

            if not data['rights']['is_owner']:
                data['time_left'] = 0

            # TODO: !!!
            # company: Company = instance
            # if data['rights']['is_owner']:
            #     rate = company.rate
            #     payment = company
            #     data['rate'] = RateSerializer(instance=instance.rate).data

        return self

    def add_employees(self):
        for data, instance in zip(self.data, self.instance):
            data['employees'] = self._SEmployee(
                instance=self._Employee.objects.filter(company_id=instance.pk),
                many=True,
            ).data

        return self


class CompanyExtendedSerializer(_Serializer):
    from holding.models.employee.serializers import EmployeeSerializer as _SEmployee
    from holding.models.employee.model import Employee as _Employee

    time_zone = _Method()

    def get_time_zone(self, model):
        return model.timezone.zone

    def add_rights(self, user):
        self.data['rights'] = {
            'is_owner': self.instance.owner_id == user.id,
            'is_manager': self.instance.owner_id == user.id,
        }

    def add_owner(self):
        self.data['owner'] = self._SEmployee(instance=self.instance.owner).data

    def add_employees(self):
        employees = self._Employee.objects.filter(company_id=self.instance.pk)

        self.data['employees'] = self._SEmployee(instance=employees, many=True).data

    class Meta:
        from holding.models.company.model import Company as _Company

        model = _Company
        fields = ('id', 'name', 'description', 'address', 'email', 'phone', 'time_zone', 'time_left')
        list_serializer_class = CompanyExtendedListSerializer
