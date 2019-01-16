from rest_framework.exceptions import APIException, NotFound


class CompanyNotFound(APIException):
    status_code = 404
    default_detail = 'Specified company not found'


class WorkerNotFound(APIException):
    status_code = 404
    default_detail = 'Specified worker not found'


class NotAllowed(APIException):
    status_code = 403
    default_detail = 'You have no permissions to do this action'
