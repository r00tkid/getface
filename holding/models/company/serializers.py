from rest_framework.serializers import ModelSerializer as _Serializer, ListSerializer as _List
from rest_framework.serializers import SerializerMethodField as _Method
from rest_framework import serializers as _se


class CompanyCreateSerializer(_Serializer):
    name = _se.CharField(
        required=True,
        allow_blank=False,
        allow_null=False,
        min_length=2,
        max_length=255,
    )

    description = _se.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
        max_length=4000,
    )

    address = _se.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
        max_length=512,
    )

    phone = _se.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
        max_length=32,
    )

    email = _se.EmailField(
        required=True,
        allow_null=False,
        allow_blank=False,
        max_length=255,
    )

    timezone = _se.CharField(
        default='UTC',
    )

    from django.db import transaction as _ts

    @_ts.atomic
    def create(self, validated_data):
        company = self.Meta.model.objects.create(**validated_data)

        company.save()

        return company

    @classmethod
    def fields_info(cls):
        return {
            'name': ('required', 'minimum chars: 2', 'maximum chars: 255',),
            'description': ('not required', 'maximum chars: 4000',),
            'address': ('not required', 'maximum chars: 512',),
            'phone': ('not required', 'maximum chars: 32',),
            'email': ('required', 'maximum chars: 255', 'valid email'),
            'timezone': ('not required', 'valid timezone',),
        }

    class Meta:
        from holding.models.company.model import Company as _Company

        model = _Company
        fields = ('name', 'description', 'address', 'phone', 'email', 'timezone',)


class CompanyUpdateSerializer(CompanyCreateSerializer):
    name = _se.CharField(
        required=False,
        allow_blank=False,
        min_length=2,
        max_length=255,
    )

    email = _se.EmailField(
        required=False,
        allow_blank=False,
        max_length=255,
    )

    def create(self, validated_data):
        raise NotImplementedError('Creation not allowed from update serializer')

    from django.db import transaction as _ts

    @_ts.atomic
    def update(self, instance, validated_data):
        """
        :type instance: holding.models.Company
        :type validated_data: dict
        """
        instance.update(validated_data, nullable=False)

        return instance

    @classmethod
    def fields_info(cls):
        return {
            **super(cls, cls).fields_info(),
            'name': ('not required', 'minimum chars: 2', 'maximum chars: 255',),
            'email': ('not required', 'maximum chars: 255', 'valid email'),
        }

    class Meta(CompanyCreateSerializer.Meta):
        pass


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
        from pytz import timezone

        if isinstance(model.timezone, str):
            return model.timezone
        else:
            return timezone(model.timezone).zone

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
