from model.heuristic import Heuristic

class ManhattanDistanceAlgorithm(Heuristic):
    def estimate(self, state):
        distance = 0
        for index, tile in enumerate(state):
            if tile == 0:
                continue
            goal_row, goal_column = divmod(tile - 1, self._size)
            current_row, current_column = divmod(index, self._size)
            distance += abs(goal_row - current_row) + abs(goal_column - current_column)
        return distance