from django.urls import path, include

# base api paths (v1)
urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('company/', include('company.urls')),
    path('agenda/', include('agenda.urls')),
]
