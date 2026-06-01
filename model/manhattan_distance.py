from model.cell import Cell
from model.heuristic import Heuristic
from model.puzzle_goal import PuzzleGoal
from model.space import Space

class ManhattanDistance(Heuristic):
    def __init__(self, size):
        super().__init__(size)
        goal = PuzzleGoal(size)
        self.__goals = {tile: goal.locate(tile) for tile in goal if tile != Cell.EMPTY}

    def estimate(self, state):
        distance = 0
        space = Space(state, self._size)
        for index, tile in enumerate(state):
            if tile == Cell.EMPTY:
                continue
            distance += self.__goals[tile].distance_to(space.decode(index))
        return distance