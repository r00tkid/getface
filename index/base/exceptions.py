import json
from rest_framework import status
from rest_framework.exceptions import APIException as RestException


class ToDo(NotImplementedError):
    pass


class APIException(RestException):

    def __init__(self, detail=None, status_code=None, code=None):
        super().__init__(detail)
        self.status_code = status_code
        self.code = code

    def __str__(self):
        if isinstance(self.detail, dict):
            return json.dumps(self.detail)
        return super(APIException, self).__str__()


class NotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Not found"


class UnprocessableEntity(APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_detail = "You're doing something wrong."
