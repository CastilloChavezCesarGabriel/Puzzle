from model.puzzle import Puzzle
from model.puzzleModel import Model
from view.puzzleView import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.puzzle = Puzzle()
        self.view = View(self)
        self.view.display(self.puzzle)
        self.solving = False

    def run(self):
        self.view.run()

    def handle_click(self, row, column):
        empty_index = self.puzzle.state.index(0)
        zx, zy = divmod(empty_index, self.puzzle.size)
        if (abs(zx - row) == 1 and zy == column) or (abs(zy - column) == 1 and zx == row):
            target = row * self.puzzle.size + column
            self.puzzle = self.puzzle.swap(empty_index, target)
            self.view.display(self.puzzle)

    def auto_shuffle(self):
        if self.solving:
            self.view.show_status("Cannot shuffle while solving...")
            return

        self.solving = True
        self.puzzle = self.puzzle.shuffle(40)
        self.view.display(self.puzzle)
        self.view.show_status("Shuffled!")
        self.solving = False

    def reset(self):
        if self.solving:
            self.view.show_status("Cannot reset while solving...")
            return

        self.solving = True
        self.puzzle = Puzzle()
        self.view.display(self.puzzle)
        self.view.show_status("Reset!")
        self.solving = False

    def solve(self):
        if self.solving:
            self.view.show_status("Already solving...")
            return

        if self.puzzle.is_solved():
            self.view.show_status("Already solved!")
            return

        self.solving = True
        self.view.show_status("Finding solution...")
        solution = self.model.solve(self.puzzle)

        if not solution:
            self.view.show_status("No solution!")
        else:
            self.view.show_solution(solution)
            self.puzzle = solution[-1]
            self.view.display(self.puzzle)
            self.view.show_status("Found!")

        self.solving = False
