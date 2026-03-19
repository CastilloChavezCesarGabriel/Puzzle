from abc import ABC, abstractmethod

class IPuzzleListener(ABC):
    @abstractmethod
    def on_click(self, row, column):
        pass

    @abstractmethod
    def on_shuffle(self):
        pass

    @abstractmethod
    def on_solve(self):
        pass

    @abstractmethod
    def on_reset(self):
        pass