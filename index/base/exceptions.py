import json
from rest_framework import status
from rest_framework.exceptions import APIException, NotFound


class BazeException(APIException):
    def __str__(self):
        if 'dict' == type(self.detail).__name__:
            return json.dumps(self.detail)
        return super(BazeException, self).__str__()


class UnprocessableEntityException(BazeException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_detail = "You're doing something wrong."
