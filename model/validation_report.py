import sys

class ValidationReport:
    def __init__(self, exception):
        self.__exception = exception
        self.__report()

    def __report(self):
        print(f"Invalid: {self.__exception}", file=sys.stderr)
        raise SystemExit(1)