from django.urls import path, include

urlpatterns = [
    path('/v1', include('index.urls.api.v1')), # base api paths
    path('/v2', include('index.urls.api.v2')), # bot api paths
]
