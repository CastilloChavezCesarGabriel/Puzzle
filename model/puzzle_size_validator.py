from model.validation_report import ValidationReport

class PuzzleSizeValidator:
    __MINIMUM = 2

    def __init__(self, value):
        try:
            self.__validate(value)
        except ValueError as exception:
            ValidationReport(exception)

    def __validate(self, value):
        if value < self.__MINIMUM:
            raise ValueError(f"puzzle size must be at least {self.__MINIMUM}, got {value}")