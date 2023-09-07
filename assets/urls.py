from django.urls import path
from .views import *


urlpatterns = [
    path('companies/',  CompanyList.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyDetail.as_view(), name='company-detail'),
    

]