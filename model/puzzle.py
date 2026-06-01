import random
from model.position import Position
from model.puzzle_goal import PuzzleGoal
from model.space import Space

class Puzzle:
    def __init__(self, size, state=None):
        self.__size = size
        self.__goal = PuzzleGoal(size)
        self.__state = state or tuple(self.__goal)

    def is_solved(self):
        return self.__goal == self.__state

    def expand(self):
        space = Space(self.__state, self.__size)
        for neighbor_index in space.expand():
            yield self.move(space.decode(neighbor_index))

    def move(self, position):
        new_state = Space(self.__state, self.__size).swap(position)
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