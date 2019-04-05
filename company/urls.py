from company.views.crud import CompanyActions
from company.views import workers, rate
from django.urls import path

urlpatterns = [
    # Companies
    path('', CompanyActions.as_view()),  # Create company (POST)
    path('/<int:company_id>', CompanyActions.as_view()),  # Company actions
    path('/<int:company_id>/me', workers.get_user_employee),  # Get worker profile for specified company
    path('/<int:company_id>/status', workers.get_user_status),  # Get status of current user for specified company

    path('/rate/available', rate.available_rates),
    path('/rate/buy', rate.company_buy_rate),
]
