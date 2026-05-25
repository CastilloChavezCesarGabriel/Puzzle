from abc import ABC, abstractmethod

class IPuzzleShuffleListener(ABC):
    @abstractmethod
    def on_shuffle(self):
        pass