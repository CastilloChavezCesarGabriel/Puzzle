import heapq

class Model:
    @staticmethod
    def solve(puzzle):
        frontier = [(puzzle.solve_by_manhattan(), 0, puzzle, None)]
        reached = {puzzle.state: 0}
        while frontier:
            _, path_cost, current_puzzle, previous_puzzle = heapq.heappop(frontier)

            if current_puzzle.is_solved():
                solution = []
                node = current_puzzle
                while node:
                    solution.append(node)
                    node = getattr(node, "_previous_puzzle", None)
                return list(reversed(solution))

            for next_puzzle in current_puzzle.move():
                new_cost = path_cost + 1
                if next_puzzle.state not in reached or new_cost < reached[next_puzzle.state]:
                    reached[next_puzzle.state] = new_cost
                    next_puzzle._previous_puzzle = current_puzzle
                    estimated_cost = new_cost + next_puzzle.solve_by_manhattan()
                    heapq.heappush(frontier, (estimated_cost, new_cost, next_puzzle, current_puzzle))
        return []