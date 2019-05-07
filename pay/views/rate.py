from rest_framework.decorators import api_view
from rest_framework.response import Response
from pay.models import Rate, RateSerializer


@api_view(['GET'])
def available(request):
    return Response({
        'detail': 'ok',
        'rates': RateSerializer(instance=Rate.objects.filter(is_archived=False), many=True).data
    })
