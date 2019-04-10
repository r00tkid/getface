from django.urls import path, include

urlpatterns = [
    # base api paths (v1)
    path('/v1', include([
        path('/auth', include('entry.urls')),
        path('/company', include('holding.urls')),
        path('/agenda', include('job.urls')),
        # path('/camera', include('cam.urls')),
    ]))
]
