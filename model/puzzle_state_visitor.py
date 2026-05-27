from abc import ABC, abstractmethod

class IPuzzleStateVisitor(ABC):
    @abstractmethod
    def visit(self, state, size):
        pass