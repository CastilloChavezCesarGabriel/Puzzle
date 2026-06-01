from abc import ABC, abstractmethod

class IPuzzleSizeListener(ABC):
    @abstractmethod
    def on_change(self, size):
        pass