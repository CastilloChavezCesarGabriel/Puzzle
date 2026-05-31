from model.validation_report import ValidationReport

class CoordinateValidator:
    def __init__(self, value):
        self.__value = value
        try:
            self.__validate()
        except ValueError as exception:
            ValidationReport(exception)

    def __validate(self):
        if self.__value < 0:
            raise ValueError(f"coordinate must be non-negative, got {self.__value}")