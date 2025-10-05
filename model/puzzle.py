import random

class Puzzle:
    def __init__(self, state=None):
        self.size = 4
        self.goal = tuple(range(1, self.size * self.size)) + (0,)
        self.state = state or self.goal

    def is_solved(self):
        return self.state == self.goal

    def move(self):
        empty_index = self.state.index(0)
        empty_row, empty_column = divmod(empty_index, self.size)
        directions = []
        if empty_row > 0:
            directions.append(-self.size)
        if empty_row < self.size - 1:
            directions.append(self.size)
        if empty_column > 0:
            directions.append(-1)
        if empty_column < self.size - 1:
            directions.append(1)
        for offset in directions:
            yield self.swap(empty_index, empty_index + offset)

    def swap(self, i, j):
        tiles_copy = list(self.state)
        tiles_copy[i], tiles_copy[j] = tiles_copy[j], tiles_copy[i]
        return Puzzle(tuple(tiles_copy))

    def shuffle(self, steps=100):
        shuffled_puzzle = self
        for i in range(steps):
            shuffled_puzzle = random.choice(list(shuffled_puzzle.move()))
        return shuffled_puzzle

    def solve_by_manhattan(self):
        distance = 0
        for i, tile in enumerate(self.state):
            if tile == 0:
                continue
            goal_row, goal_column = divmod(tile - 1, self.size)
            current_row, current_column = divmod(i, self.size)
            distance += abs(goal_row - current_row) + abs(goal_column - current_column)
        return distance

    def __lt__(self, other):
        return self.state < other.state