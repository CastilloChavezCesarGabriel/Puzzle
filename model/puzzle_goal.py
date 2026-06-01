from model.cell import Cell
from model.space import Space

class PuzzleGoal:
    def __init__(self, size):
        self.__arrangement = tuple(range(1, size * size)) + (Cell.EMPTY,)
        self.__space = Space(self.__arrangement, size)

    def __iter__(self):
        return iter(self.__arrangement)

    def __eq__(self, other):
        if isinstance(other, PuzzleGoal):
            return self.__arrangement == other.__arrangement
        return self.__arrangement == other

    def __hash__(self):
        return hash(self.__arrangement)

    def locate(self, tile):
        return self.__space.decode(self.__arrangement.index(tile))