from abc import ABC, abstractmethod

class IPuzzleResetListener(ABC):
    @abstractmethod
    def on_reset(self):
        pass