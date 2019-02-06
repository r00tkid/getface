from django.urls import path
from employee.views.crud import EmployeeActions

urlpatterns = [
    path('/worker', EmployeeActions.as_view()),  # Create worker (POST)
    # path('/workers', workers.get_company_workers),  # Get company workers
    path('/worker/<int:worker_id>', EmployeeActions.as_view()),  # Other workers crud
]
