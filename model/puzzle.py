import random
from model.position import Position
from model.puzzle_size_validator import PuzzleSizeValidator
from model.puzzle_state_validator import PuzzleStateValidator
from model.space import Space
from model.tile import Tile

class Puzzle:
    def __init__(self, size, state=None):
        PuzzleSizeValidator(size)
        PuzzleStateValidator(state, size)
        self.__size = size
        self.__goal = tuple(range(1, size * size)) + (0,)
        self.__state = state or self.__goal

    def is_solved(self):
        return self.__state == self.__goal

    def expand(self):
        for neighbor_index in Space(self.__state, self.__size).expand():
            yield self.move(Position(*divmod(neighbor_index, self.__size)))

    def move(self, position):
        new_state = Tile(position).move(self.__state, self.__size)
        if new_state is None:
            return self
        return Puzzle(self.__size, new_state)

    def shuffle(self, steps):
        shuffled = self
        previous = None
        for _ in range(steps):
            moves = list(shuffled.expand())
            if previous:
                moves = [move for move in moves if move != previous] or moves
            previous, shuffled = shuffled, random.choice(moves)
        return shuffled

    def accept(self, visitor):
        for row in range(self.__size):
            for column in range(self.__size):
                position = Position(row, column)
                visitor.visit(row, column, self.__state[position.flatten(self.__size)])

    def estimate(self, heuristic):
        return heuristic.estimate(self.__state)

    def reset(self):
        return Puzzle(self.__size)

    def __eq__(self, other):
        return isinstance(other, Puzzle) and self.__state == other.__state

    def __hash__(self):
        return hash(self.__state)