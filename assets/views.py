from rest_framework import generics
from .models import (
    Company,
    Employee,
    Device,
    DeviceAssignment
)
from .serializers import (
    CompanySerializer,
    EmployeeSerializer,
    DeviceSerializer,
    DeviceAssignmentSerializer

)



class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyCreate(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer



class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeCreate(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DeviceList(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceCreate(generics.CreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer



class DeviceAssignmentList(generics.ListCreateAPIView):
    queryset = DeviceAssignment.objects.all()
    serializer_class = DeviceAssignmentSerializer


class DeviceAssignmentCreate(generics.CreateAPIView):
    queryset = DeviceAssignment.objects.all()
    serializer_class = DeviceAssignmentSerializer


class DeviceAssignmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceAssignment.objects.all()
    serializer_class = DeviceAssignmentSerializer

    


