import math
from model.puzzle_search import IPuzzleSearch

class IterativeDeepeningSearch(IPuzzleSearch):
    __SOLVED = -1

    def __init__(self, puzzle, heuristic):
        self.__heuristic = heuristic
        self.__root = puzzle
        self.__path = [puzzle]
        self.__visited = {puzzle}

    def run(self):
        bound = self.__root.estimate(self.__heuristic)
        while True:
            result = self.__search(0, bound)
            if result == self.__SOLVED:
                return list(self.__path)
            if result == math.inf:
                return []
            bound = result

    def __search(self, cost, bound):
        current = self.__path[-1]
        estimated = cost + current.estimate(self.__heuristic)
        if estimated > bound:
            return estimated
        if current.is_solved():
            return self.__SOLVED
        minimum = math.inf

        for neighbor in current.expand():
            if neighbor in self.__visited:
                continue
            self.__path.append(neighbor)
            self.__visited.add(neighbor)
            result = self.__search(cost + 1, bound)
            if result == self.__SOLVED:
                return self.__SOLVED
            if result < minimum:
                minimum = result
            self.__path.pop()
            self.__visited.discard(neighbor)
        return minimum