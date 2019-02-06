from rest_framework.decorators import api_view, permission_classes
from company.base.permissions import CanManageCompany
from rest_framework.response import Response
from rest_framework import status
from employee.models import Employee
from company.models import Company


@api_view(('GET',))
@permission_classes((CanManageCompany,))
def get_company_employees(request, company_id):
    query = request.GET

    if query.get('all') == '':
        objects = Employee.model().all
    else:
        objects = Employee.model().objects

    objects = objects.filter(company_id=company_id)

    is_fired = query.get('fired')
    is_manager = query.get('manager')
    is_employee = query.get('employee')

    if is_fired != '':
        objects = objects.filter(is_fired=False)

    if is_manager is not is_employee:
        if is_manager == '':
            objects = objects.filter(is_manager=True)

        if is_employee == '':
            objects = objects.filter(is_manager=False)

    return Response(
        {
            'detail': 'Employees view',
            'employees': Employee.serializer('extended')(
                objects,
                many=True,
            ).data,
        }, status=status.HTTP_200_OK
    )


@api_view(('GET',))
# Default auth permission
def get_user_status(request, company_id):
    company = Company.info(company_id, 'extended').instance
    user = request.user

    employee = Employee.model().objects.filter(user=user, company=company).first()
    deleted = Employee.model().all.filter(user=user, company=company).first()

    return Response({
        'is_owner': company.owner_id == user.id,
        'is_employee': bool(employee),
        'is_manager': employee.is_manager if bool(employee) else False,
        'is_fired': employee.is_fired if bool(employee) else True if company.owner_id != user.id else False,
        'is_deleted': bool(deleted.deleted_at) if deleted else False,
    })


@api_view(('GET',))
# Default auth permission
def get_user_employee(request, company_id):
    company = Company.info(company_id, 'extended').Meta.model
    user = request.user
    employee = Employee.model().objects.filter(user=user, company=company).first()

    return Response({
        'detail': 'Your company profile' if employee else 'You are not the part of this company or not in employees',
        'employee': Employee.serializer('extended')(instance=employee).data if employee else None,
    }, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION if employee else status.HTTP_403_FORBIDDEN)
