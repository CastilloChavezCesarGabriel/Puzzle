from controller.cell_display_visitor import CellDisplayVisitor
from model.position import Position
from view.puzzle_click_listener import IPuzzleClickListener
from view.puzzle_reset_listener import IPuzzleResetListener
from view.puzzle_shuffle_listener import IPuzzleShuffleListener
from view.puzzle_size_listener import IPuzzleSizeListener
from view.puzzle_solve_listener import IPuzzleSolveListener

class PuzzleController(IPuzzleClickListener, IPuzzleShuffleListener, IPuzzleSolveListener,
                      IPuzzleResetListener, IPuzzleSizeListener):
    __NOTIFICATION_DURATION = 2000
    __SHUFFLE_GUARD_MESSAGE = "Cannot shuffle while solving..."
    __RESET_GUARD_MESSAGE = "Cannot reset while solving..."
    __SOLVE_GUARD_MESSAGE = "Already solving..."
    __SIZE_CHANGE_GUARD_MESSAGE = "Cannot change size while solving..."

    def __init__(self, game, view):
        self.__game = game
        self.__view = view
        self.__solving = False
        self.__view.bind(self)

    def run(self):
        self.__view.run()

    def on_click(self, row, column):
        if self.__game.move(Position(row, column), self.__view, self.__NOTIFICATION_DURATION):
            self.__refresh()

    def on_shuffle(self):
        if self.__guard(self.__SHUFFLE_GUARD_MESSAGE):
            return
        self.__lock()
        self.__game.shuffle(self.__view, self.__NOTIFICATION_DURATION)
        self.__settle()

    def on_reset(self):
        if self.__guard(self.__RESET_GUARD_MESSAGE):
            return
        self.__lock()
        self.__game.reset(self.__view, self.__NOTIFICATION_DURATION)
        self.__settle()

    def on_solve(self):
        if self.__guard(self.__SOLVE_GUARD_MESSAGE):
            return
        self.__lock()
        self.__game.solve(self.__view, self.__NOTIFICATION_DURATION)
        self.__settle()

    def on_change(self, size):
        if self.__guard(self.__SIZE_CHANGE_GUARD_MESSAGE):
            return
        self.__game.resize(size)
        self.__view.rebuild(size, self)
        self.__refresh()

    def __refresh(self):
        self.__game.accept(CellDisplayVisitor(self.__view))

    def __guard(self, message):
        if self.__solving:
            self.__view.notify(message, self.__NOTIFICATION_DURATION)
            return True
        return False

    def __lock(self):
        self.__solving = True

    def __settle(self):
        self.__refresh()
        self.__solving = False