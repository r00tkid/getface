from django.urls import re_path
from django.views.generic import View
from django.shortcuts import render


# Cause we have SPA all request for frontend goes here
class Index(View):
    @staticmethod
    def get(request):
        return render(request, 'index.html')


urlpatterns = [
    re_path(r'^(?!static|media|api|favicon.ico|admin).*', Index.as_view()),
]
