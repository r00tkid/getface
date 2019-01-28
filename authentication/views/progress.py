from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from authentication.models import Feature, Progress


@api_view(['GET'])
def add_progress(request, feature_id):
    Progress.model()(
        user=request.user,
        feature=Feature.info(feature_id).instance,
    ).save()

    return Response({
        'detail': 'Feature with id:[%(feature)d] has been added to progress' % {'feature': feature_id}
    }, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def remove_progress(request, feature_id):
    Progress.model().objects.get(
        user=request.user,
        feature=Feature.info(feature_id).instance
    ).delete()

    return Response({
        'detail': 'Feature with id:[%(feature)d] has been removed from progress' % {'feature': feature_id}
    })
