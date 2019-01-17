from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class AgendaActions(APIView):
    http_method_names = ['get', 'post', 'put', 'delete', 'restore', 'purge']

    def post(self, request):
        return Response(data={
            'detail': 'Agenda has been created',
            'agenda': 'a',
            'request': request.data,
            'method': request.method,
        }, status=status.HTTP_201_CREATED)

    def get(self, request):
        return Response(data={
            'detail': 'Agenda has been found',
            'agenda': 'a',
            'request': request.data,
            'method': request.method,
        }, status=status.HTTP_201_CREATED)

    def put(self, request):
        return Response(data={
            'detail': 'Agenda has been updated',
            'agenda': 'a',
            'request': request.data,
            'method': request.method,
        }, status=status.HTTP_201_CREATED)

    def delete(self, request):
        return Response(data={
            'detail': 'Agenda has been deleted',
            'agenda': 'a',
            'request': request.data,
            'method': request.method,
        }, status=status.HTTP_201_CREATED)

    def restore(self, request):
        return Response(data={
            'detail': 'Agenda has been restored',
            'agenda': 'a',
            'request': request.data,
            'method': request.method,
        }, status=status.HTTP_201_CREATED)

    def purge(self, request):
        return Response(data={
            'detail': 'Agenda has been purged',
            'agenda': 'a',
            'request': request.data,
            'method': request.method,
        }, status=status.HTTP_201_CREATED)
