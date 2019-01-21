from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from tech import base


@api_view(['GET'])
@permission_classes((AllowAny,))
def sign_in(request):
    return Response({
        'detail': 'Default login form'
    })


@api_view(['GET'])
@permission_classes((AllowAny,))
def sign_up(request):
    from tech.form.autentication import Registration
    return Response(base.get_form_fields(Registration()))


@api_view(['GET'])
@permission_classes((AllowAny,))
def worker_sign_up(request):
    from tech.form.autentication import WorkerRegistration
    return Response(base.get_form_fields(WorkerRegistration))


@api_view(['GET'])
@permission_classes((AllowAny,))
def check_checker(request):
    from index.base.validation import StandAloneValidator

    validator = StandAloneValidator({
        'one': 1,
        'two': 2,
    }, {
        'one': 'min:2|max:0',
        'two': {'min': 3, 'max': 1},
    })

    validator.validate(True, "Invalid data")
