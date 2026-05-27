import random
from model.space import Space
from model.tile import Tile

class Puzzle:
    def __init__(self, size, state=None):
        self.__size = size
        self.__goal = tuple(range(1, size * size)) + (0,)
        self.__state = state or self.__goal

    def is_solved(self):
        return self.__state == self.__goal

    def expand(self):
        for _, neighbor_index in Space().expand(self.__state, self.__size):
            row, column = divmod(neighbor_index, self.__size)
            yield self.move(row, column)

    def move(self, row, column):
        new_state = Tile(row, column).move(self.__state, self.__size)
        if new_state is None:
            return self
        return Puzzle(self.__size, new_state)

    def shuffle(self, steps):
        shuffled = self
        previous = None
        for step in range(steps):
            moves = list(shuffled.expand())
            if previous:
                moves = [move for move in moves if move != previous] or moves
            previous, shuffled = shuffled, random.choice(moves)
        return shuffled

    def accept(self, visitor):
        visitor.visit(self.__state, self.__size)

    def estimate(self, heuristic):
        return heuristic.estimate(self.__state)

    def reset(self):
        return Puzzle(self.__size)

    def __eq__(self, other):
        return isinstance(other, Puzzle) and self.__state == other.__state

    def __hash__(self):
        return hash(self.__state)