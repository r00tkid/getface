from django.urls import path, include

# base api paths (v1)
urlpatterns = [
    path('post/', include('post.urls')),
]
