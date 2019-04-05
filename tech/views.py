import subprocess

from authentication.models import get_user_by_id
from index.mail import sender
from tech import base

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http.response import HttpResponse
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes((AllowAny,))
def fortune(request):
    return HttpResponse(
        b"<pre id='fortune'>%s</pre>" % subprocess.Popen(
            '/usr/games/fortune | /usr/games/cowthink',
            shell=True,
            stdout=subprocess.PIPE,
        ).stdout.read(),
    )


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
    return Response(base.get_form_fields(User.validators.create))


@api_view(['GET'])
@permission_classes((AllowAny,))
def worker_sign_up(request):
    from employee.models import Employee

    return Response(base.get_form_fields(Employee.validators.activate))


@api_view(['GET'])
@permission_classes((AllowAny,))
def user_data_ext(request, user_id):
    from authentication.views.auth import _user_response

    return _user_response(get_user_by_id(user_id))


@api_view(['GET'])
@permission_classes((AllowAny,))
def user_data_companies(request, user_id):
    from authentication.views.auth import _user_response

    return _user_response(get_user_by_id(user_id), with_companies=True)
