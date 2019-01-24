from index.base.repository import Base
from index.base.exceptions import NotFound
from index import settings


class CompanyRepository(Base):

    @classmethod
    def model(cls):
        from .model import Company

        return Company

    @classmethod
    def admin_view(cls):
        from .admin import Company

        return Company

    @classmethod
    def actions(cls):
        from .validator import Create, Update

        return {
            'create': Create,
            'update': Update
        }

    @classmethod
    def serializers(cls):
        from .serializer import BaseCompany, ExtendedCompany

        return {
            'base': BaseCompany,
            'extended': ExtendedCompany,
        }
