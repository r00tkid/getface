from rest_framework.decorators import api_view
from rest_framework.response import Response
from company.models import Company, Payment, Rate, Discount


@api_view(['POST'])
def add_payment(request):
    company = Company.info(request.data.get('company_id'))

    payment = Payment.model()(
        user=request.user,
        rate_id=request.data.get('rate_id'),
        discount_id=company.instance.discount_id,
        info=request.data.get('info'),
        company=company.instance,
    )

    payment.save()

    company_model: Company.model() = company.instance
    company_model.payment = payment
    company_model.save()

    return Response({
        'detail': 'Payment has been saved',
        'company': company.data,
    })


@api_view(['GET'])
def payments(request, company_id):
    payment = Payment.model()
    company = Company.info(company_id)

    return Response({
        'detail': 'Payments for [%s] company' % company.instance.name,
        'payments': Payment.serializer()(instance=payment.objects.filter(company=company.instance), many=True).data
    })


@api_view(['GET'])
def company_rate(request, company_id):
    company = Company.info(company_id)

    return Response({
        'detail': 'Rate for [%s] company' % company.instance.name,
        'rate': Rate.serializer()(instance=company.instance.rate).data,
        'discount': Discount.serializer()(instance=company.instance.discount).data
    })
