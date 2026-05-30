from abc import ABC, abstractmethod

class IPuzzleCellVisitor(ABC):
    @abstractmethod
    def visit(self, row, column, value):
        pass