from django.urls import path
from company.worker.actions import WorkerActions
from . import views

urlpatterns = [
    # Companies
    path('', views.create_company),  # Company info
    path('/<int:company_id>', views.get_company_view),  # Company info

    # Workers
    path('/<int:company_id>/worker', WorkerActions.as_view()),  # Create worker (POST)
    path('/<int:company_id>/workers', views.get_company_workers),  # Get company workers
    path('/<int:company_id>/worker/<int:worker_id>', WorkerActions.as_view()),  # Other workers crud
]
