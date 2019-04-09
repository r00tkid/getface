from django.urls import path, include

urlpatterns = [
    # base api paths (v1)
    path('/v1', include({
        'app_name': 'api.v1',
        'url_patterns': [
            path('/auth', include('auth.urls')),
            path('/company', include('gang.urls')),
            path('/agenda', include('job.urls')),
            path('/camera', include('cam.urls')),
        ]
    }))
]
