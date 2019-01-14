from django.urls import path
from .worker.crud import WorkerCrud
from . import views

urlpatterns = [
    # Companies
    path('', views.create_company),  # Company info
    path('/<int:company_id>', views.get_company_view),  # Company info

    # Workers
    path('/<int:company_id>/worker', WorkerCrud.as_view()),  # Create worker (POST)
    path('/<int:company_id>/workers', views.get_company_workers),  # Get company workers
    path('/<int:company_id>/worker/<int:worker_id>', WorkerCrud.as_view()),  # Other workers crud
]
