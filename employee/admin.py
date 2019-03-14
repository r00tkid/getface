from django.contrib import admin
from employee.models import Employee, Department, Position

admin.site.register(Employee.model, Employee.admin)
admin.site.register(Department.model)
admin.site.register(Position.model)
