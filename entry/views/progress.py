from entryentication.models import Progress, get_feature_by_id as _get_feature
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def add_progress(request, feature_id):
    Progress.model(
        user=request.user,
        feature=_get_feature(feature_id),
    ).save()

    return Response({
        'detail': 'Feature with id:[%(feature)d] has been added to progress' % {'feature': feature_id}
    }, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def remove_progress(request, feature_id):
    Progress.model().objects.get(
        user=request.user,
        feature=_get_feature(feature_id)
    ).delete()

    return Response({
        'detail': 'Feature with id:[%(feature)d] has been removed from progress' % {'feature': feature_id}
    })
