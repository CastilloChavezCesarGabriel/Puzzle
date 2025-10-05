import heapq

class Solver:
    @staticmethod
    def solve(puzzle):
        frontier = [(puzzle.solve_by_manhattan(), 0, puzzle, [])]
        reached = set()
        while frontier:
            _, path_cost, current_puzzle, path = heapq.heappop(frontier)
            if current_puzzle.is_solved():
                return path + [current_puzzle]
            if current_puzzle.state in reached:
                continue
            reached.add(current_puzzle.state)

            for next_puzzle in current_puzzle.move():
                new_cost = path_cost + 1
                estimated_cost = new_cost + next_puzzle.solve_by_manhattan()
                heapq.heappush(frontier, (estimated_cost, new_cost, next_puzzle, path + [current_puzzle]))
        return []