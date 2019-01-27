from django.urls import path
from company.views.company.crud import CompanyActions
from company.views.company import workers
from company.views.worker.crud import WorkerActions

urlpatterns = [
    # Companies
    path('', CompanyActions.as_view()),  # Create company (POST)
    path('/<int:company_id>', CompanyActions.as_view()),  # Company actions
    path('/<int:company_id>/me', workers.get_user_worker),  # Get worker profile for specified company
    path('/<int:company_id>/status', workers.get_user_status),  # Get status of current user for specified company

    # Workers
    path('/<int:company_id>/worker', WorkerActions.as_view()),  # Create worker (POST)
    path('/<int:company_id>/workers', workers.get_company_workers),  # Get company workers
    path('/<int:company_id>/worker/<int:worker_id>', WorkerActions.as_view()),  # Other workers crud
]
