from controller.cell_display_visitor import CellDisplayVisitor

class PuzzleAnimationSolver:
    __ALREADY_SOLVED_MESSAGE = "Already solved!"
    __SOLVING_MESSAGE = "Solving puzzle..."
    __NO_SOLUTION_MESSAGE = "No solution!"
    __SOLVED_MESSAGE = "Solved!"

    def __init__(self, model, view):
        self.__model = model
        self.__view = view

    def solve(self, puzzle, duration):
        if puzzle.is_solved():
            self.__view.notify(self.__ALREADY_SOLVED_MESSAGE, duration)
            return puzzle

        self.__view.notify(self.__SOLVING_MESSAGE, None)
        solution = self.__model.solve(puzzle)

        if not solution:
            self.__view.notify(self.__NO_SOLUTION_MESSAGE, duration)
            return puzzle

        self.__view.animate(solution, CellDisplayVisitor(self.__view))
        self.__view.notify(self.__SOLVED_MESSAGE, duration)
        return solution.conclude()