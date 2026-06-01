from abc import ABC, abstractmethod

class IPuzzleSearch(ABC):
    @abstractmethod
    def run(self):
        pass