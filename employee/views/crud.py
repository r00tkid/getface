import uuid
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from authentication.models import User
from employee.models import Employee


class EmployeeActions(APIView):
    # permission_classes = (CanManageEmployees,)
    http_method_names = ['get', 'post', 'invite', 'faceid', 'put', 'delete', 'restore', 'purge', 'fire', 'hire']

    def post(self, request, company_id):
        validator = Employee.action('create')(data=request.data)

        if not validator.validate():
            return Response({
                'detail': 'Form not valid',
                'errors': validator.errors,
            })

        data = validator.data

        try:
            employee = Employee.model().objects.get(email=data.get('email'), company_id=company_id)

            return Response({
                'detail': 'Employee with current mail already exists in your company',
                'employee': Employee.serializer()(instance=employee).data,
            }, status=status.HTTP_207_MULTI_STATUS)
        except:
            pass

        employee = Employee.new({
            'first_name': data.get('first_name'),
            'last_name': data.get('last_name'),
            'email': data.get('email'),
            'phone': data.get('phone') if data.get('phone') and data.get('phone') != '' else None,
            'company_id': company_id,
        })

        try:
            user = User.model().objects.get(email=data.get('email'))

            employee.user_id = user.id
        except:
            user = User.new({
                'username': uuid.uuid4(),
                'email': data.get('email'),
                'first_name': data.get('first_name'),
                'last_name': data.get('last_name'),
                'is_active': False,
            })

            user.set_password(user.username)
            user.save()

        # In first place I was thinking to send mail on creating, but than mechanics has change
        employee.save()

        return Response(data={
            'detail': 'Employee has been created',
            'employee': Employee.serializer('extended')(instance=employee).data,
        }, status=status.HTTP_201_CREATED)

    def invite(self, request, employee_id, company_id):
        data: dict = request.data
        s_employee = Employee.info(pk=employee_id)
        o_employee: Employee.model() = s_employee.instance

        if o_employee.is_active:
            return Response({
                'detail': 'Employee activated already'
            }, status=status.HTTP_409_CONFLICT)

        previous_invitation = o_employee.new_invitation()
        o_employee.is_invited = True
        o_employee.save()

        return Response({
            'detail': 'Employee has been invited',
            'previous_invitation': previous_invitation,
        })

    def faceid(self, request, employee_id, company_id):
        data: dict = request.data
        s_employee = Employee.info(pk=employee_id)
        o_employee: Employee.model() = s_employee.instance

        if data.get('remove'):
            o_employee.clear_face_id()
            o_employee.save()

            return Response({
                'detail': 'Employee face-id has been removed.'
            })

        o_employee.new_face_id()
        o_employee.save()

        return Response({
            'detail': 'Employee face-id has been updated',
            'face_id': o_employee.face_id,
        })

    def get(self, request, employee_id, company_id):
        options = request.GET

        if options.get('all') != '':
            employee = Employee.model().objects
        else:
            employee = Employee.model().all

        try:
            return Response({
                'detail': 'Employee has been found',
                'employee': Employee.serializer('extended')(instance=employee.get(id=employee_id)).data
            })
        except:
            return Response(data={
                'detail': 'Employee has not been found',
            }, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, employee_id, company_id):
        validator = Employee.action('update')(data=request.data)

        if not validator.validate():
            return Response({
                'detail': 'Your data is invalid',
                'errors': validator.errors,
            })

        employee = Employee.model().objects.get(pk=employee_id).update(validator.data, nullable=False)

        return Response(data={
            'detail': 'Employee has been updated',
            'employee': Employee.serializer('extended')(instance=employee).data,
        })

    def delete(self, request, employee_id, company_id):
        employee = Employee.model().objects.get(pk=employee_id)

        employee.delete()

        return Response(data={
            'detail': 'Employee %s %s has been deleted' % (employee.first_name, employee.last_name),
            'employee': Employee.serializer('extended')(instance=employee).data,
        })

    def restore(self, request, employee_id, company_id):
        employee = Employee.model().deleted.get(pk=employee_id)

        employee.deleted_at = None
        employee.save()

        return Response({
            'detail': 'Employee %s %s has been restored' % (employee.first_name, employee.last_name),
            'employee': Employee.info('extended')(instance=employee).data
        })

    def purge(self, request, employee_id, company_id):
        employee = Employee.model().objects.get(pk=employee_id)

        employee.hard_delete()

        return Response(data={
            'detail': 'Employee %s %s has been fully removed from system' % (employee.first_name, employee.last_name),
            'employee': Employee.serializer('extended')(instance=employee).data,
        })

    def fire(self, request, employee_id, company_id):
        employee = Employee.model().objects.get(pk=employee_id)

        employee.is_fired = True
        employee.save()

        return Response({
            'detail': 'Employee has been fired',
            'employee': Employee.serializer('extended')(instance=employee).data,
        })

    def hire(self, request, employee_id, company_id):
        employee = Employee.model().objects.get(pk=employee_id)

        employee.is_fired = False
        employee.save()

        return Response({
            'detail': 'Employee has been hired',
            'employee': Employee.serializer('extended')(instance=employee).data,
        })
