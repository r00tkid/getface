# All imports here is for Django to see those models and for better use experience
from holding.models.company import Company, CompanyAdmin, CompanySerializer, CompanyExtendedSerializer, CompanyExtendedListSerializer
from holding.models.department import Department, DepartmentAdmin, DepartmentSerializer
from holding.models.employee import Employee, EmployeeAdmin, EmployeeSerializer, EmployeeExtendedSerializer
from holding.models.position import Position, PositionToDepartment, PositionAdmin, PositionSerializer

# Getters
from app.base.helpers import get_model as __get


@__get(model=Company)
def get_company(id, raise_exception=True, obj=None) -> Company:
    return obj


@__get(model=Department)
def get_department(id, raise_exception=True, obj=None) -> Department:
    return obj


@__get(model=Employee)
def get_employee(id, raise_exception=True, obj=None) -> Employee:
    return obj


@__get(model=Position)
def get_position(id, raise_exception=True, obj=None) -> Position:
    return obj
