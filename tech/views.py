from tech import base
from index.mail import sender
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes((AllowAny,))
def turtle(request):
    sender.Sandman(
        mail_to="abnormally.dev@gmail.com",
        body="Test mail",
        subject="Non default",
    ).start()

    return Response({
        'detail': 'All is ok'
    })


@api_view(['GET'])
@permission_classes((AllowAny,))
def sign_in(request):
    return Response({
        'detail': 'Default login form'
    })


@api_view(['GET'])
@permission_classes((AllowAny,))
def sign_up(request):
    from authentication.models import User
    return Response(base.get_form_fields(User.action('register')))


@api_view(['GET'])
@permission_classes((AllowAny,))
def worker_sign_up(request):
    from company.models import Worker
    return Response(base.get_form_fields(Worker.action('register')))
