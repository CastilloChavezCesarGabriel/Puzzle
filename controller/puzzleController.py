from model.puzzle import Puzzle

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.puzzle = Puzzle()
        self.view = view
        self.solving = False
        self.duration = 3000

        self.view.on_click_tile = self.handle_click
        self.view.on_shuffle = self.auto_shuffle
        self.view.on_solve = self.solve
        self.view.on_reset = self.reset

        self.view.display(self.puzzle)

    def run(self):
        self.view.run()

    def handle_click(self, row, column):
        new_puzzle = self.puzzle.move_tile(row, column)
        if new_puzzle != self.puzzle:
            self.puzzle = new_puzzle
            self.view.display(self.puzzle)
            if self.puzzle.is_solved():
                self.view.show_status("Solved!", self.duration)

    def auto_shuffle(self):
        if self.solving:
            self.view.show_status("Cannot shuffle while solving...", self.duration)
            return

        self.solving = True
        self.puzzle = self.puzzle.shuffle(40)
        self.view.display(self.puzzle)
        self.view.show_status("Shuffled!", self.duration)
        self.solving = False

    def reset(self):
        if self.solving:
            self.view.show_status("Cannot reset while solving...", self.duration)
            return

        self.solving = True
        self.puzzle = Puzzle()
        self.view.display(self.puzzle)
        self.view.show_status("Reset!", self.duration)
        self.solving = False

    def solve(self):
        if self.solving:
            self.view.show_status("Already solving...", self.duration)
            return

        if self.puzzle.is_solved():
            self.view.show_status("Already solved!", self.duration)
            return

        self.solving = True
        self.view.show_status("Solving puzzle...", None)
        solution = self.model.solve(self.puzzle)

        if not solution:
            self.view.show_status("No solution!", self.duration)
        else:
            self.view.show_solution(solution)
            self.puzzle = solution[-1]
            self.view.display(self.puzzle)
            self.view.show_status("Solved!", self.duration)

        self.solving = False