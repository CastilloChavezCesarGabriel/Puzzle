import heapq
import itertools

class HeuristicPuzzleSearch:
    def __init__(self, puzzle, heuristic):
        self.__puzzle = puzzle
        self.__heuristic = heuristic
        self.__counter = itertools.count()
        self.__frontier = []
        self.__history = {}

    def run(self):
        estimated = self.__puzzle.estimate(self.__heuristic)
        self.__frontier = [(estimated, next(self.__counter), self.__puzzle)]
        self.__history = {self.__puzzle: (0, None)}
        return self.__explore()

    def __explore(self):
        while self.__frontier:
            _, _, current = heapq.heappop(self.__frontier)
            if current.is_solved():
                return self.__trace(current)
            for neighbor in current.expand():
                self.__process(neighbor, current)
        return []

    def __process(self, neighbor, current):
        new_cost = self.__history[current][0] + 1
        existing = self.__history.get(neighbor)
        if existing is None or new_cost < existing[0]:
            self.__history[neighbor] = (new_cost, current)
            estimated = new_cost + neighbor.estimate(self.__heuristic)
            heapq.heappush(self.__frontier, (estimated, next(self.__counter), neighbor))

    def __trace(self, current):
        solution = []
        node = current
        while node is not None:
            solution.append(node)
            node = self.__history[node][1]
        return list(reversed(solution))