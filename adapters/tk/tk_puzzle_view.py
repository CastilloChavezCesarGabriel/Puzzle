import tkinter as tk
import time
from adapters.tk.tk_board import TkBoard
from adapters.tk.tk_control_panel import TkControlPanel
from adapters.tk.tk_status_bar import TkStatusBar
from view.puzzle_view import IPuzzleView

class TkPuzzleView(IPuzzleView):
    __WOOD_BACKGROUND = "#c38a06"
    __ANIMATION_DELAY_SECONDS = 0.3

    def __init__(self, size, controls):
        self.__root = tk.Tk()
        self.__root.title("Puzzle")
        self.__root.configure(background=TkPuzzleView.__WOOD_BACKGROUND)
        self.__status_bar = TkStatusBar(self.__root, TkPuzzleView.__WOOD_BACKGROUND)
        self.__board = TkBoard(self.__root, TkPuzzleView.__WOOD_BACKGROUND, size)
        self.__control_panel = TkControlPanel(self.__root, TkPuzzleView.__WOOD_BACKGROUND, controls)

    def bind(self, listener):
        self.__board.bind(listener)
        self.__control_panel.bind(listener)

    def display(self, state, size):
        self.__board.display(state, size)

    def animate(self, steps, visitor):
        for step in steps:
            step.accept(visitor)
            self.__root.update()
            time.sleep(TkPuzzleView.__ANIMATION_DELAY_SECONDS)

    def notify(self, text, duration=None):
        self.__status_bar.show(text, duration)

    def run(self):
        self.__root.mainloop()