from abc import ABC, abstractmethod

class IPuzzleView(ABC):
    @abstractmethod
    def display(self, row, column, value):
        pass

    @abstractmethod
    def animate(self, steps, visitor):
        pass

    @abstractmethod
    def notify(self, text, duration=None):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def bind(self, listener):
        pass

    @abstractmethod
    def rebuild(self, size, listener):
        pass