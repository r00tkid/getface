# All models imports just for django to see them
from company.models.company.model import Company as CompanyModel
from company.models.rate.model import Rate as RateModel
from company.models.payment.model import Payment as PaymentModel
from company.models.discount.model import Discount as DiscountModel

# Worker models
from company.models.worker.model import Worker as WorkerModel
from company.models.worker.department.model import WorkerDepartment as DepartmentModel
from company.models.worker.position.model import WorkerPosition as PositionModel

from company.models.company.repository import CompanyRepository as Company
from company.models.rate.repository import RateRepository as Rate
from company.models.payment.repository import PaymentRepository as Payment
from company.models.discount.repository import DiscountRepository as Discount

# Worker repositories
from company.models.worker.repository import WorkerRepository as Worker
from company.models.worker.department.repository import DepartmentRepository as Department
from company.models.worker.position.repository import PositionRepository as Position
