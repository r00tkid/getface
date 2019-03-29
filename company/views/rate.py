from index.base.exceptions import APIException
from rest_framework.decorators import api_view
from rest_framework.response import Response
from company.models import Rate, Company, Payment
from authentication.models import User


@api_view(['GET'])
def available_rates(request):
    return Response({
        'detail': 'ok',
        'rates': Rate.serializers.base(instance=Rate.model.objects.filter(is_archived=False), many=True).data
    }, 200)


@api_view(['POST'])
def company_buy_rate(request):
    company = Company.model.objects.filter(pk=request.data.get('company_id')).first()
    rate = Rate.model.objects.filter(pk=request.data.get('rate_id')).first()
    user: User.model = request.user

    if not company:
        raise APIException({
            'detail': "No such company"
        }, 404)

    if not rate:
        raise APIException({
            'detail': "No such rate"
        }, 404)

    if company.owner.id != user.id:
        raise APIException({
            'detail': "No permissions"
        }, 403)

    if company.rate is not None and company.time_left.total_seconds() > 0:
        raise APIException({
            'detail': "There is one already"
        }, 409)

    details = Payment.details(company=company, rate=rate)
    details.save()

    # ToDo: remove @test from details
    payment = Payment.model(user=user, discount=company.discount, details=details, info='{"type":"@test"}')
    payment.save()

    return Response({
        'detail': "Payment successful",
        # ToDo: owner status
        'company': Company.serializers.extended(instance=company).data,
    }, 200)
