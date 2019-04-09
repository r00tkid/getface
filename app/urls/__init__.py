from django.contrib.admin import site as admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.urls),  # One of the kind, dmn
    path('api', include('app.urls.api')),
    path('', include('app.urls.web')),
]
