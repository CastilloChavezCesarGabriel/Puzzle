from model.puzzle import Puzzle
from model.puzzleModel import Model
from view.puzzleView import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.puzzle = Puzzle()
        self.view = View(self)
        self.view.display(self.puzzle)

    def run(self):
        self.view.run()

    def handle_click(self, row, column):
        empty_index = self.puzzle.state.index(0)
        zx, zy = divmod(empty_index, self.puzzle.size)
        if (abs(zx - row) == 1 and zy == column) or (abs(zy - column) == 1 and zx == row):
            target = row * self.puzzle.size + column
            self.puzzle = self.puzzle.swap(empty_index, target)
            self.view.display(self.puzzle)
            if self.puzzle.is_solved():
                self.view.show_status("All done!")

    def auto_shuffle(self):
        self.puzzle = self.puzzle.shuffle(30)
        self.view.display(self.puzzle)
        self.view.show_status("Shuffled!")

    def reset(self):
        self.puzzle = Puzzle()
        self.view.display(self.puzzle)
        self.view.show_status("Reset!")

    def solve(self):
        solution = self.model.solve(self.puzzle)
        if not solution:
            self.view.show_status("No solution!")
            return
        self.view.show_status("Finding solution...")
        self.view.show_solution(solution)
        self.puzzle = solution[-1]
        self.view.display(self.puzzle)
        self.view.show_status("Found!")
