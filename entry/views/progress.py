from entry.models import Progress, Feature
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def add_progress(request, feature_id):
    Progress(
        user=request.user,
        feature=Feature.get_by_id(feature_id),
    ).save()

    return Response({
        'detail': 'Feature with id:[%(feature)d] has been added to progress' % {'feature': feature_id}
    }, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def remove_progress(request, feature_id):
    Progress.objects.get(
        user=request.user,
        feature=Feature.get_by_id(feature_id)
    ).delete()

    return Response({
        'detail': 'Feature with id:[%(feature)d] has been removed from progress' % {'feature': feature_id}
    })
