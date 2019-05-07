from django.urls import re_path, path, include
from django.contrib.admin import site as admin
from django.views.generic import View
from django.shortcuts import render


# Cause we have SPA all request for frontend goes here
class Index(View):
    @staticmethod
    def get(request):
        return render(request, 'index.html')


urlpatterns = [
    path('admin/', admin.urls),

    # API
    path('api', include([

        # V1
        path('/v1', include([
            path('/auth', include('entry.urls')),
            path('/company', include('holding.urls')),

            path('/job', include('job.urls')),
            path('/camera', include('cam.urls')),
            path('/payment', include('pay.urls')),
        ]))

    ])),

    # All other requested paths goes to index
    re_path(r'^(?!static|media|api|favicon.ico|admin).*', Index.as_view()),
]
