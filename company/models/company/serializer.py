from index.base.repository import Base
from authentication.models import User
from company.models.company.model import Company
from company.models.worker.model import Worker
from company.models.worker.serializer import BaseWorker, ExtendedWorker


def get_worker_serializer(name):
    return {
        'base': BaseWorker,
        'extended': ExtendedWorker,
    }[name]


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
            if not user:
                data[field_name] = None
            else:
                data[field_name] = BaseWorker(
                    instance=Worker.objects.filter(user=user, company=instance).first()
                ).data

    def add_workers(self, name='base'):
        for data, instance in zip(self.data, self.instance):
            serial = get_worker_serializer(name)

            data['workers'] = serial(
                instance=Worker.objects.filter(company_id=instance.pk),
                many=True,
            ).data

    def update(self, instance, validated_data):
        super().update(instance, validated_data)


class ExtendedCompany(Base.Serializer):
    def add_owner(self):
        self.data['owner'] = User.serializer()(instance=self.instance.owner).data

    def add_workers(self):
        workers = Worker.objects.filter(company_id=self.instance.pk)

        self.data['workers'] = BaseWorker(instance=workers, many=True).data

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'address', 'email', 'phone')
        list_serializer_class = ExtendedCompanyList
