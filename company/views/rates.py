from rest_framework.decorators import api_view
from rest_framework.response import Response
from company.models import Rate


@api_view(['GET'])
def available_rates(request):
    if not request.user:
        return Response({
            'detail': 'Bad user auth',
        }, 403)

    return Response({
        'detail': 'ok',
        'rates': Rate.serializers.base(instance=Rate.model.objects.filter(is_archived=False), many=True).data
    }, 200)
