from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response


class WorkerCrud(APIView):
    # Change to IsAuthenticated
    permission_classes = AllowAny

    def post(self, request):
        return Response(data={
            'message': 'Create worker',
            'method': request.method,
        }, status=status.HTTP_201_CREATED)

    def get(self, request, worker_id):
        return Response(data={
            'message': 'Get [%s] worker' % worker_id,
            'method': request.method,
        })

    def put(self, request, worker_id):
        return Response(data={
            'message': 'Get [%s] worker' % worker_id,
            'method': request.method,
        })


def get_worker(request, worker_id):
    return {
        'data': {
            'name': 'get id:[%s] worker' % worker_id,
        }, 'status': status.HTTP_200_OK
    }


def update_worker(request, worker_id):
    return {
        'data': {
            'name': 'get id:[%s] worker' % worker_id,
        }, 'status': status.HTTP_200_OK
    }


def delete_worker(request, worker_id):
    return {
        'data': {
            'name': 'get id:[%s] worker' % worker_id,
        }, 'status': status.HTTP_200_OK
    }


def purge_worker(request, worker_id):
    return {
        'data': {
            'name': 'get id:[%s] worker' % worker_id,
        }, 'status': status.HTTP_200_OK
    }
