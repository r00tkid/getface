from django.urls import path, include

# other api paths
urlpatterns = [
    path('/form', include('tech.urls'))
]
