from company.models import Company, Payment, Rate, Discount, get_company_by_id as _get_company
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def add_payment(request):
    company = _get_company(request.data.get('company_id'))

    payment = Payment.model(
        user=request.user,
        rate_id=request.data.get('rate_id'),
        discount_id=company.instance.discount_id,
        info=request.data.get('info'),
        company=company.instance,
    )

    payment.save()

    company.payment = payment
    company.save()

    return Response({
        'detail': 'Payment has been saved',
        'company': Company.serializers.extended(instance=company).data,
    })


@api_view(['GET'])
def payments(request, company_id):
    company = _get_company(company_id)

    return Response({
        'detail': 'Payments for [%s] company' % company.instance.name,
        'payments': Payment.serializers.base(instance=Payment.model.objects.filter(company=company), many=True).data
    })


@api_view(['GET'])
def company_rate(request, company_id):
    company = _get_company(company_id)

    return Response({
        'detail': 'Rate for [%s] company' % company.instance.name,
        'rate': Rate.serializers.base(instance=company.instance.rate).data,
        'discount': Discount.serializers.base(instance=company.instance.discount).data
    })
