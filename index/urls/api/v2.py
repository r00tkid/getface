from django.urls import path, include

# other api paths
urlpatterns = [
    path('/tech', include('tech.urls'))
]
