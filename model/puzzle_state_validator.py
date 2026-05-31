from model.validation_report import ValidationReport

class PuzzleStateValidator:
    def __init__(self, values, size):
        self.__values = values
        self.__size = size
        try:
            self.__validate()
        except ValueError as exception:
            ValidationReport(exception)

    def __validate(self):
        if self.__values is None:
            return
        if sorted(self.__values) != list(range(self.__size * self.__size)):
            raise ValueError(f"state {tuple(self.__values)} is not a valid arrangement for size {self.__size}")