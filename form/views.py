from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from . import base


@api_view(['GET'])
@permission_classes([AllowAny])
def sign_in(request):
    pass


@api_view(['GET'])
@permission_classes([AllowAny])
def sign_up(request):
    from .modules.autentication import Registration
    return Response(base.get_form_fields(Registration()))
