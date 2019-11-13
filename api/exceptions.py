from abc import ABC, abstractmethod

class PhotoChallengeException(ABC, Exception):
    @abstractmethod
    def error_message(self) -> str:
        return "An unknown error has occurred."

    @abstractmethod
    def status_code(self) -> int:
        return 500

class MethodNotFound(PhotoChallengeException):
    def __init__(self, path: str, method: str) -> None:
        self.path = path
        self.method = method

    def error_message(self) -> str:
        return "(%s) '/api/%s' does not exist." % (self.method, self.path)

    def status_code(self) -> int:
        return 404

class MissingParameter(PhotoChallengeException):
    def __init__(self, parameter_name: str, parameter_type) -> None:
        self.parameter_name = parameter_name
        self.parameter_type = parameter_type

    def error_message(self) -> str:
        return "Required parameter '%s' (%s) is missing." % (self.parameter_name, self.parameter_type.__name__)

    def status_code(self) -> int:
        return 400

class ParameterCasting(PhotoChallengeException):
    def __init__(self, parameter_name: str, parameter_type, string_value: str) -> None:
        self.parameter_name = parameter_name
        self.parameter_type = parameter_type
        self.string_value = string_value

    def error_message(self) -> str:
        return "Parameter '%s' of type %s has an invalid value: '%s'" % (self.parameter_name, self.parameter_type.__name__, self.string_value)

    def status_code(self) -> int:
        return 400

