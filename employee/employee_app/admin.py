from django.contrib import admin
from . models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'department', 'company_name', 'joining_year')
    search_fields = ('employee_id', 'name', 'department')
    list_filter = ('department', 'company_name')