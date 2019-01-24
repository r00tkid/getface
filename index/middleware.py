from . import settings
from rest_framework.response import Response


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if settings.DEBUG and 'OPTIONS' == request.method:
            response = Response(
                data={
                    'detail': 'Options set in headers',
                },
                status=200,
                headers={
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "GET, OPTIONS, POST, DELETE, PUT, PURGE",
                    "Access-Control-Allow-Headers": "Content-type, Authorization, X-Requested-With, X-XSRF-TOKEN",
                    #"Access-Control-Allow-Credentials": True,
                    "Access-Control-Max-Age": 10000,
                })

            old = self.get_response(request)
            response.accepted_renderer = old.accepted_renderer
            response.accepted_media_type = old.accepted_media_type
            response.renderer_context = {}
        else:
            response = self.get_response(request)

        return response
