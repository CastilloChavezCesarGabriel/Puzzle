from model.heuristic import Heuristic

class ManhattanDistance(Heuristic):
    def __init__(self, size):
        super().__init__(size)
        self.__goals = tuple(divmod(tile - 1, size) for tile in range(size * size))

    def estimate(self, state):
        distance = 0
        for index, tile in enumerate(state):
            if tile == 0:
                continue
            goal_row, goal_column = self.__goals[tile]
            current_row, current_column = divmod(index, self._size)
            distance += abs(goal_row - current_row)
            distance += abs(goal_column - current_column)
        return distance