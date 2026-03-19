import heapq

class Model:
    def __init__(self):
        self.__frontier = []
        self.__reached = {}
        self.__parents = {}

    def solve(self, puzzle):
        self.__frontier = [(puzzle.solve_by_manhattan(), 0, puzzle)]
        self.__reached = {puzzle: 0}
        self.__parents = {puzzle: None}
        return self.__search()

    def __search(self):
        while self.__frontier:
            _, _, current_puzzle = heapq.heappop(self.__frontier)
            if current_puzzle.is_solved():
                return self.__trace(current_puzzle)
            for next_puzzle in current_puzzle.move():
                self.__process(next_puzzle, current_puzzle)
        return []

    def __trace(self, current_puzzle):
        solution = []
        node = current_puzzle
        while node is not None:
            solution.append(node)
            node = self.__parents.get(node)
        return list(reversed(solution))

    def __process(self, next_puzzle, current_puzzle):
        new_cost = self.__reached[current_puzzle] + 1
        if next_puzzle not in self.__reached or new_cost < self.__reached[next_puzzle]:
            self.__reached[next_puzzle] = new_cost
            self.__parents[next_puzzle] = current_puzzle
            estimated_cost = new_cost + next_puzzle.solve_by_manhattan()
            heapq.heappush(self.__frontier, (estimated_cost, new_cost, next_puzzle))