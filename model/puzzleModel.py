import heapq

class Model:
    def __init__(self):
        self.frontier = []
        self.reached = {}

    def solve(self, puzzle):
        self.frontier = [(puzzle.solve_by_manhattan(), 0, puzzle, None)]
        self.reached = {puzzle.state: 0}
        while self.frontier:
            _, path_cost, current_puzzle, previous_puzzle = heapq.heappop(self.frontier)

            if current_puzzle.is_solved():
                return self.create_solution(current_puzzle)

            for next_puzzle in current_puzzle.move():
                self.process(next_puzzle, current_puzzle, path_cost)

        return []

    @staticmethod
    def create_solution(current_puzzle):
        solution = []
        node = current_puzzle
        while node:
            solution.append(node)
            node = getattr(node, "_previous_puzzle", None)
        return list(reversed(solution))

    def process(self, next_puzzle, current_puzzle, path_cost):
        new_cost = path_cost + 1
        if next_puzzle.state not in self.reached or new_cost < self.reached[next_puzzle.state]:
            self.reached[next_puzzle.state] = new_cost
            next_puzzle._previous_puzzle = current_puzzle
            estimated_cost = new_cost + next_puzzle.solve_by_manhattan()
            heapq.heappush(self.frontier, (estimated_cost, new_cost, next_puzzle, current_puzzle))
