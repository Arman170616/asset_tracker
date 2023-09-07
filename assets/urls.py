from django.urls import path
from .views import *


urlpatterns = [
    path('companies/',  CompanyList.as_view(), name='company-list'),
    path('companies/create/', CompanyCreate.as_view(), name='company-create'),
    path('companies/<int:pk>/', CompanyDetail.as_view(), name='company-detail'),
    path('companies/<int:pk>/delete', CompanyDetail.as_view(), name='company-delete'),


    path('employees/',  EmployeeList.as_view(), name='employee-list'),
    path('employees/create/', EmployeeCreate.as_view(), name='employee-create'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
    path('employees/<int:pk>/delete', EmployeeDetail.as_view(), name='employee-delete'),
    
    

]