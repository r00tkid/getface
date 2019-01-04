from django.urls import re_path
from app.views import Index

urlpatterns = [
    re_path(r'^(?!static|media|api|favicon.ico|admin).*', Index.as_view()),
]
