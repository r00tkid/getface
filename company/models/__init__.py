# All models imports just for django to see them
from company.models.company.model import Company as CompanyModel
from company.models.rate.model import Rate as RateModel
from company.models.payment.model import Payment as PaymentModel
from company.models.discount.model import Discount as DiscountModel

from company.models.company.repository import Repository as Company
from company.models.rate.repository import Repository as Rate
from company.models.payment.repository import Repository as Payment
from company.models.discount.repository import Repository as Discount


def get_company_by_id(company_id, raise_exception=True) -> Company.model():
    from index.base.exceptions import APIException

    company = Company.model.objects.filter(pk=company_id).first()

    if not company and raise_exception:
        raise APIException({
            'detail': 'Company not found'
        }, status_code=404)

    return company


def get_rate_by_id(rate_id, raise_exception=True) -> Rate.model():
    from index.base.exceptions import APIException

    rate = Rate.model.objects.filter(pk=rate_id).first()

    if not rate and raise_exception:
        raise APIException({
            'detail': 'Rate not found'
        }, status_code=404)

    return rate


def get_payment_by_id(payment_id, raise_exception=True) -> Payment.model():
    from index.base.exceptions import APIException

    payment = Payment.model.objects.filter(pk=payment_id).first()

    if not payment and raise_exception:
        raise APIException({
            'detail': 'Payment not found'
        }, status_code=404)

    return payment


def get_discount_by_id(discount_id, raise_exception=True) -> Discount.model():
    from index.base.exceptions import APIException

    discount = Discount.model.objects.filter(pk=discount_id).first()

    if not discount and raise_exception:
        raise APIException({
            'detail': 'Discount not found'
        }, status_code=404)

    return discount
