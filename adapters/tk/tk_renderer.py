from abc import ABC, abstractmethod

class TkRenderer(ABC):
    @abstractmethod
    def render(self, tile, value):
        pass