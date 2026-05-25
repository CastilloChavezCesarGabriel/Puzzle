from abc import ABC, abstractmethod

class IPuzzleButton(ABC):
    @abstractmethod
    def configure(self, widget, listener):
        pass