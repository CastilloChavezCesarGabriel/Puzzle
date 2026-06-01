from abc import ABC, abstractmethod

class Heuristic(ABC):
    def __init__(self, size):
        self._size = size

    @abstractmethod
    def estimate(self, state):
        pass