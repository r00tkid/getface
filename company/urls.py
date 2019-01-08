from django.urls import path, include
from . import views

company_urls = [
    path('', views.get_companies),
    path('<int:company_id>', views.get_company_view),
    path('<int:company_id>/workers', views.get_company_workers),
]

worker_urls = [
    path('', views.get_workers),
]

urlpatterns = [
    path('', include(company_urls)),  # Base companies paths
    path('worker/', include(worker_urls)),  # Base workers paths
]
