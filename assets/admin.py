from django.contrib import admin

from .models import *


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'email', 'website', 'description', 'created_at')


admin.site.register(Company, CompanyAdmin)

