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

    def move_tile(self, row, column):
        empty_index = self.state.index(0)
        zx, zy = divmod(empty_index, self.size)

        if (abs(zx - row) == 1 and zy == column) or (abs(zy - column) == 1 and zx == row):
            target_index = row * self.size + column
            return self.swap(empty_index, target_index)

        return self

    def swap(self, i, j):
        tiles_copy = list(self.state)
        tiles_copy[i], tiles_copy[j] = tiles_copy[j], tiles_copy[i]
        return Puzzle(tuple(tiles_copy))

    def shuffle(self, steps):
        shuffled = self
        previous = None
        for i in range(steps):
            moves = list(shuffled.move())
            if previous:
                moves = [move for move in moves if move.state != previous.state] or moves
            previous, shuffled = shuffled, random.choice(moves)
        return shuffled

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
        return self.solve_by_manhattan() < other.solve_by_manhattan()