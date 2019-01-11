from django.urls import path, include, re_path
from . import views

company_urls = [
    path('', views.get_companies),
    path('/<int:company_id>', views.get_company_view),
    path('/<int:company_id>/workers', views.get_company_workers),
]

worker_urls = [
    path('', views.create_worker),
    path('/<int:worker_id>', views.crud_worker),
]

urlpatterns = [
    path('', include(company_urls)),  # Base companies paths
    path('/worker', include(worker_urls)),  # Base workers paths
]
