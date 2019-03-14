from employee.models.employee.model import Employee as EmployeeModel
from employee.models.department.model import Department as DepartmentModel
from employee.models.position.model import Position as PositionModel

from employee.models.employee.repository import Repository as Employee
from employee.models.department.repository import Repository as Department
from employee.models.position.repository import Repository as Position


def get_employee_by_id(employee_id, raise_exception=True) -> Employee.model():
    from index.base.exceptions import APIException

    employee = Employee.model.objects.filter(pk=employee_id).first()

    if not employee and raise_exception:
        raise APIException({
            'detail': 'Employee not found'
        }, status_code=404)

    return employee


def get_department_by_id(department_id, raise_exception=True) -> Department.model():
    from index.base.exceptions import APIException

    department = Department.model.objects.filter(pk=department_id).first()

    if not department and raise_exception:
        raise APIException({
            'detail': 'Department not found'
        }, status_code=404)

    return department


def get_position_by_id(position_id, raise_exception=True) -> Position.model():
    from index.base.exceptions import APIException

    position = Position.model.objects.filter(pk=position_id).first()

    if not position and raise_exception:
        raise APIException({
            'detail': 'Position not found'
        }, status_code=404)

    return position
