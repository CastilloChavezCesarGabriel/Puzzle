import heapq
import itertools

class HeuristicSearch:
    def __init__(self, puzzle, heuristic):
        self.__heuristic = heuristic
        self.__counter = itertools.count()
        priority = puzzle.estimate(heuristic)
        self.__frontier = [(priority, next(self.__counter), puzzle)]
        self.__history = {puzzle: (0, None)}

    def run(self):
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