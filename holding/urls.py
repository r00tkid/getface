from django.urls import path, include
from .views import company, department, employee, position

urlpatterns = [
    # Company
    path('', company.create),

    path('/<int:pk>', include([

        path('/crud', company.CompanyCrudView.as_view())

    ])),

    # Department
    path('/department', include([

        path('', department.create),

        path('/<int:pk>', include([

            path('/crud', department.DepartmentCrudView.as_view())

        ])),

    ])),

    # Employee
    path('/employee', include([

        path('', employee.create),

        path('/<int:pk>', include([

            path('/crud', employee.EmployeeCrudView.as_view())

        ])),

    ])),

    # Position
    path('/position', include([

        path('', position.create),

        path('/<int:pk>', include([

            path('/crud', position.PositionCrudView.as_view())

        ])),

    ])),
]
