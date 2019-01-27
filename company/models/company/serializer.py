from index.base.repository import Base
from company.models.company.model import Company
from authentication.models import User
from company.models import Worker


class BaseCompany(Base.Serializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'address', 'email', 'phone')


class ExtendedCompany(Base.Serializer):
    def add_owner(self):
        self.fields.fields.__setattr__('owner', User.serializer('base')(instance=self.Meta.model.owner).data)

    def add_workers(self):
        workers = Worker.model().objects.filter(company_id=self.Meta.model.pk)

        self.fields.fields.__setattr__('workers', Worker.serializer('base')(instance=workers, many=True))

    class Meta:
        model = Company
        fields = ['id', 'name', 'description', 'address', 'email', 'phone']
