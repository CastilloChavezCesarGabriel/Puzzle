from abc import ABC, abstractmethod

class IPuzzleClickListener(ABC):
    @abstractmethod
    def on_click(self, position):
        pass