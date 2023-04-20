from django.contrib import admin
from API.models import Company , Employee
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location', 'type')

class EmployeeaAdmin(admin.ModelAdmin):
    list_display= ('name', 'email', 'company')

admin.site.register(Employee, EmployeeaAdmin)
admin.site.register(Company, CompanyAdmin)