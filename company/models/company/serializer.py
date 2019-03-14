from index.base.repository import Base
from company.models.company.model import Company
from company.models.rate.serializer import RateSerializer
from authentication.models import User
from employee.models import Employee


class CompanySerializer(Base.Serializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'address', 'email', 'phone')


class CompanyExtendedListSerializer(Base.ListSerializer):
    def add_owner(self):
        for data, instance in zip(self.data, self.instance):
            data['owner'] = User.serializers.base(instance=instance.owner).data

        return self

    def add_rights(self, user, add_employee_info=False):
        for data, instance in zip(self.data, self.instance):
            employee = Employee.model.objects.filter(user=user, company=instance).first()

            data['as_employee'] = Employee.serializers.base(
                instance=Employee.model.objects.filter(user=user, company=instance).first()
            ).data if employee and add_employee_info else None

            data['rights'] = {
                'is_owner': instance.owner_id == user.id,
                'is_manager': employee.is_manager if employee else False or instance.owner_id == user.id,
            }

            # TODO: !!!
            # company: Company = instance
            # if data['rights']['is_owner']:
            #     rate = company.rate
            #     payment = company
            #     data['rate'] = RateSerializer(instance=instance.rate).data

        return self

    def add_employee_info(self, user=None, field_name='employee'):
        for data, instance in zip(self.data, self.instance):
            if not user:
                data[field_name] = None
            else:
                data[field_name] = Employee.serializers.base(
                    instance=Employee.model.objects.filter(user=user, company=instance).first()
                ).data

        return self

    def add_employees(self):
        for data, instance in zip(self.data, self.instance):
            data['employees'] = Employee.serializers.extended(
                instance=Employee.model.objects.filter(company_id=instance.pk),
                many=True,
            ).data

        return self


class CompanyExtendedSerializer(Base.Serializer):
    serializers = Base.serializers

    time_zone = serializers.SerializerMethodField()

    def get_time_zone(self, model):
        return model.timezone.zone

    def add_owner(self):
        self.data['owner'] = User.serializers.base(instance=self.instance.owner).data

    def add_employees(self):
        employees = Employee.model.objects.filter(company_id=self.instance.pk)

        self.data['employees'] = Employee.serializers.base(instance=employees, many=True).data

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'address', 'email', 'phone', 'time_zone', 'time_left')
        list_serializer_class = CompanyExtendedListSerializer
