from index.base.repository import Base
from company.models.company.model import Company
from authentication.models import User
from company.models import Worker


class BaseCompany(Base.Serializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'address', 'email', 'phone')


class ExtendedCompanyList(Base.ListSerializer):
    def add_owner(self):
        for data, instance in zip(self.data, self.instance):
            data['owner'] = User.serializer()(instance=instance.owner).data

    def add_worker_info(self, user=None, field_name='worker'):
        for data, instance in zip(self.data, self.instance):
            if not User:
                data[field_name] = None
            else:
                data[field_name] = Worker.serializer()(
                    instance=Worker.model().objects.filter(user=user, company=instance).first()
                ).data

    def add_workers(self, name='base'):
        for data, instance in zip(self.data, self.instance):
            data['workers'] = Worker.serializer(name)(
                instance=Worker.model().objects.filter(company_id=instance.pk),
                many=True,
            ).data

    def update(self, instance, validated_data):
        super().update(instance, validated_data)


class ExtendedCompany(Base.Serializer):
    def add_owner(self):
        self.data['owner'] = User.serializer()(instance=self.instance.owner).data

    def add_workers(self):
        workers = Worker.model().objects.filter(company_id=self.instance.pk)

        self.data['workers'] = Worker.serializer()(instance=workers, many=True).data

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'address', 'email', 'phone')
        list_serializer_class = ExtendedCompanyList
