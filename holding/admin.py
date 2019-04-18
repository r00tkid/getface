from django.contrib import admin
from .models import Company, CompanyAdmin, CompanyCreator, Department, DepartmentAdmin, Employee, EmployeeAdmin, Position, PositionAdmin, PositionToDepartment

admin.site.register(Company, CompanyAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position, PositionAdmin)
# admin.site.register(PositionToDepartment)
# admin.site.register(CompanyCreator)
