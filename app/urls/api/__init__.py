from django.urls import path, include

urlpatterns = [
    path('/v1', include('app.urls.api.v1')), # base api paths
    path('/v2', include('app.urls.api.v2')), # bot api paths
]
