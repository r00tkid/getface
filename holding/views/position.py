from holding.models import Position, PositionSerializer
from rest_framework.decorators import api_view
from app.base.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


@api_view(['CREATE'])
def create(request):
    creating = PositionSerializer(data=request.data)

    if not creating.is_valid():
        raise APIException({
            'detail': 'Invalid data',
            'errors': creating.errors,
        }, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    creating.save()

    return Response({
        'detail': 'Created',
        'company': creating.data,
    })


class PositionCrudView(APIView):
    http_method_names = ('get', 'update', 'delete',)

    def get(self, request, pk):
        return Response({
            'detail': 'Found',
            'company': PositionSerializer(instance=Position.get_by_id(pk)).data,
        })

    def update(self, request, pk):
        # ToDo: (Ack) update serializer
        updating = PositionSerializer(instance=Position.get_by_id(pk), data=request.data)

        if not updating.is_valid():
            raise APIException({
                'detail': 'Invalid data',
                'errors': updating.errors,
            }, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

        updating.save()

        return Response({
            'detail': 'Updated',
            'company': updating.data,
        })

    def delete(self, request, pk):
        return Response({
            'detail': 'Deleted',
            'deleted': Position.get_by_id(pk).delete(),
        })
