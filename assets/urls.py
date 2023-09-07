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

    
    path('devices/',  DeviceList.as_view(), name='device-list'),
    path('devices/create/', DeviceCreate.as_view(), name='device-create'),
    path('devices/<int:pk>/', DeviceDetail.as_view(), name='device-detail'),
    path('devices/<int:pk>/delete', DeviceDetail.as_view(), name='device-delete'),


    path('assignments/',  DeviceAssignmentList.as_view(), name='assignment-list'),
    path('assignments/create/', DeviceAssignmentCreate.as_view(), name='assignment-create'),
    path('assignments/<int:pk>/', DeviceAssignmentDetail.as_view(), name='assignment-detail'),
    path('assignments/<int:pk>/delete', DeviceAssignmentDetail.as_view(), name='assignment-delete'),
    

]