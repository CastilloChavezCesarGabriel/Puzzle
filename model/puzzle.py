import random

from model.manhattan_distance import ManhattanDistance
from model.tile import Tile

class Puzzle:
    def __init__(self, state=None):
        self.__size = 4
        self.__goal = tuple(range(1, self.__size * self.__size)) + (0,)
        self.__state = state or self.__goal

    def is_solved(self):
        return self.__state == self.__goal

    def move(self):
        empty_index = self.__state.index(0)
        empty_row, empty_column = divmod(empty_index, self.__size)
        directions = []
        if empty_row > 0:
            directions.append(-self.__size)
        if empty_row < self.__size - 1:
            directions.append(self.__size)
        if empty_column > 0:
            directions.append(-1)
        if empty_column < self.__size - 1:
            directions.append(1)
        for offset in directions:
            yield self.__swap(empty_index, empty_index + offset)

    def move_tile(self, row, column):
        new_state = Tile(row, column).move(self.__state, self.__size)
        if new_state is None:
            return self
        return Puzzle(new_state)

    def __swap(self, first_index, second_index):
        tiles_copy = list(self.__state)
        tiles_copy[first_index], tiles_copy[second_index] = tiles_copy[second_index], tiles_copy[first_index]
        return Puzzle(tuple(tiles_copy))

    def shuffle(self, steps):
        shuffled = self
        previous = None
        for step in range(steps):
            moves = list(shuffled.move())
            if previous:
                moves = [move for move in moves if move != previous] or moves
            previous, shuffled = shuffled, random.choice(moves)
        return shuffled

    def accept(self, visitor):
        visitor.visit(self.__state, self.__size)

    def solve_by_manhattan(self):
        return ManhattanDistance(self.__size).estimate(self.__state)

    def __lt__(self, other):
        return self.solve_by_manhattan() < other.solve_by_manhattan()

    def __eq__(self, other):
        return isinstance(other, Puzzle) and self.__state == other.__state

    def __hash__(self):
        return hash(self.__state)