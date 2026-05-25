from view.puzzle_listener import IPuzzleListener

class Controller(IPuzzleListener):
    def __init__(self, model, view, puzzle):
        self.__model = model
        self.__puzzle = puzzle
        self.__view = view
        self.__solving = False
        self.__duration = 2000
        self.__view.add(self)
        self.__display()

    def visit(self, state, size):
        self.__view.display(state, size)

    def run(self):
        self.__view.run()

    def on_click(self, row, column):
        new_puzzle = self.__puzzle.move(row, column)
        if new_puzzle != self.__puzzle:
            self.__puzzle = new_puzzle
            self.__display()
            if self.__puzzle.is_solved():
                self.__view.notify("Solved!", self.__duration)

    def on_shuffle(self):
        if self.__guard("Cannot shuffle while solving..."):
            return

        self.__puzzle = self.__puzzle.shuffle(40)
        self.__display()
        self.__view.notify("Shuffled!", self.__duration)
        self.__solving = False

    def on_reset(self):
        if self.__guard("Cannot reset while solving..."):
            return

        self.__puzzle = self.__puzzle.reset()
        self.__display()
        self.__view.notify("Reset!", self.__duration)
        self.__solving = False

    def on_solve(self):
        if self.__puzzle.is_solved():
            self.__view.notify("Already solved!", self.__duration)
            return

        if self.__guard("Already solving..."):
            return

        self.__resolve()
        self.__solving = False

    def __resolve(self):
        self.__view.notify("Solving puzzle...", None)
        solution = self.__model.solve(self.__puzzle)
        if not solution:
            self.__view.notify("No solution!", self.__duration)
            return
        self.__view.animate(solution, self)
        self.__puzzle = solution[-1]
        self.__display()
        self.__view.notify("Solved!", self.__duration)

    def __display(self):
        self.__puzzle.accept(self)

    def __guard(self, message):
        if self.__solving:
            self.__view.notify(message, self.__duration)
            return True
        self.__solving = True
        return False