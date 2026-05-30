from controller.puzzle_animation_solver import PuzzleAnimationSolver
from controller.puzzle_mover import PuzzleMover
from controller.puzzle_resetter import PuzzleResetter
from controller.puzzle_shuffler import PuzzleShuffler
from model.position import Position
from model.puzzle_cell_visitor import IPuzzleCellVisitor
from view.puzzle_click_listener import IPuzzleClickListener
from view.puzzle_reset_listener import IPuzzleResetListener
from view.puzzle_shuffle_listener import IPuzzleShuffleListener
from view.puzzle_solve_listener import IPuzzleSolveListener

class PuzzleController(IPuzzleClickListener, IPuzzleShuffleListener, IPuzzleSolveListener, IPuzzleResetListener, IPuzzleCellVisitor):
    __NOTIFICATION_DURATION = 2000
    __SHUFFLE_GUARD_MESSAGE = "Cannot shuffle while solving..."
    __RESET_GUARD_MESSAGE = "Cannot reset while solving..."
    __SOLVE_GUARD_MESSAGE = "Already solving..."

    def __init__(self, model, view, puzzle):
        self.__model = model
        self.__puzzle = puzzle
        self.__view = view
        self.__solving = False
        self.__refresh()
        self.__view.bind(self)

    def visit(self, row, column, value):
        self.__view.display(row, column, value)

    def run(self):
        self.__view.run()

    def on_click(self, row, column):
        mover = PuzzleMover(self.__view, PuzzleController.__NOTIFICATION_DURATION)
        new_puzzle = mover.move(self.__puzzle, Position(row, column))
        if new_puzzle != self.__puzzle:
            self.__puzzle = new_puzzle
            self.__refresh()

    def on_shuffle(self):
        if self.__guard(PuzzleController.__SHUFFLE_GUARD_MESSAGE):
            return

        shuffler = PuzzleShuffler(self.__view, PuzzleController.__NOTIFICATION_DURATION)
        self.__puzzle = shuffler.shuffle(self.__puzzle)

        self.__refresh()
        self.__solving = False

    def on_reset(self):
        if self.__guard(PuzzleController.__RESET_GUARD_MESSAGE):
            return

        resetter = PuzzleResetter(self.__view, PuzzleController.__NOTIFICATION_DURATION)
        self.__puzzle = resetter.reset(self.__puzzle)

        self.__refresh()
        self.__solving = False

    def on_solve(self):
        if self.__guard(PuzzleController.__SOLVE_GUARD_MESSAGE):
            return

        solver = PuzzleAnimationSolver(self.__model, self.__view, self)
        self.__puzzle = solver.solve(self.__puzzle, PuzzleController.__NOTIFICATION_DURATION)

        self.__refresh()
        self.__solving = False

    def __refresh(self):
        self.__puzzle.accept(self)

    def __guard(self, message):
        if self.__solving:
            self.__view.notify(message, PuzzleController.__NOTIFICATION_DURATION)
            return True
        self.__solving = True
        return False