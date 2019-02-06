from django.urls import path
from company.views import workers
from company.views.crud import CompanyActions

urlpatterns = [
    # Companies
    path('', CompanyActions.as_view()),  # Create company (POST)
    path('/<int:company_id>', CompanyActions.as_view()),  # Company actions
    path('/<int:company_id>/me', workers.get_user_employee),  # Get worker profile for specified company
    path('/<int:company_id>/status', workers.get_user_status),  # Get status of current user for specified company
]
