from abc import ABC, abstractmethod
from model.puzzle_size_validator import PuzzleSizeValidator

class Heuristic(ABC):
    def __init__(self, size):
        PuzzleSizeValidator(size)
        self._size = size

    @abstractmethod
    def estimate(self, state):
        pass