from rest_framework.exceptions import APIException as RestException
from rest_framework import status


class ToDo(NotImplementedError):
    pass


class APIException(RestException):
    def __init__(self, detail=None, status_code=None, code=None):
        super().__init__(detail, code)
        self.status_code = status_code


class NotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Not found"

    def __init__(self, detail=None, code=None):
        if not detail:
            detail = {
                'detail': self.default_detail,
            }

        super().__init__(detail, status.HTTP_404_NOT_FOUND, code)


class UnprocessableEntity(APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_detail = "You're doing something wrong."
