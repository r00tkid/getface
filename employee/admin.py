from employee.models import Employee, Department, Position
from django.contrib import admin

admin.site.register(Employee.model, Employee.admin)
admin.site.register(Department.model)
admin.site.register(Position.model)
