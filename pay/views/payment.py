from holding.models import Company, CompanyExtendedSerializer, Employee
from pay.models import Rate, Payment, PaymentDetails
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.base.exceptions import APIException


@api_view(['POST'])
def buy_rate(request):
    company = Company.objects.filter(pk=request.data.get('company_id')).first()
    rate = Rate.objects.filter(pk=request.data.get('rate_id')).first()
    user = request.user

    if not company:
        raise APIException({
            'detail': "No such company"
        }, 404)

    if not rate:
        raise APIException({
            'detail': "No such rate"
        }, 404)

    employee = Employee.objects.filter(user=request.user, company=company).first()

    if not employee or company.owner.id != employee.id:
        raise APIException({
            'detail': "No permissions"
        }, 403)

    if company.rate is not None and company.time_left.total_seconds() > 0:
        raise APIException({
            'detail': "There is one already"
        }, 409)

    details = PaymentDetails(company=company, rate=rate)
    details.save()

    # ToDo: remove @test from details
    payment = Payment(user=user, discount=company.discount, details=details, info='{"type":"@test"}')
    payment.save()

    serializer = CompanyExtendedSerializer(instance=company)
    serializer.add_rights(user)

    return Response({
        'detail': "Payment successful",
        'company': serializer.data,
    }, 200)
