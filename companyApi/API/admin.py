from django.contrib import admin
from API.models import Company , Employee
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location', 'type')
    search_fields= ('name',)

class EmployeeaAdmin(admin.ModelAdmin):
    list_display= ('name', 'email', 'company')
    list_filter=('company',)
    
admin.site.register(Employee, EmployeeaAdmin)
admin.site.register(Company, CompanyAdmin)