from django.contrib import admin

from .models import *


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'email', 'website', 'description', 'created_at')


admin.site.register(Company, CompanyAdmin)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'position', 'created_at')
    list_filter = ('company', 'position')
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Device)
admin.site.register(DeviceAssignment)


