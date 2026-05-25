from abc import ABC, abstractmethod

class IPuzzleSolveListener(ABC):
    @abstractmethod
    def on_solve(self):
        pass