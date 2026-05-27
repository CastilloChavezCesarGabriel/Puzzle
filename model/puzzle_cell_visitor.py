from abc import ABC, abstractmethod

class IPuzzleCellVisitor(ABC):
    @abstractmethod
    def visit(self, position, value):
        pass