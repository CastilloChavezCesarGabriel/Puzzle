import tkinter as tk
import time
from adapters.tk.tk_board import TkBoard
from adapters.tk.tk_control_panel import TkControlPanel
from adapters.tk.tk_puzzle_dropdown import TkPuzzleDropdown
from adapters.tk.tk_status_bar import TkStatusBar
from view.puzzle_view import IPuzzleView

class TkPuzzleView(IPuzzleView):
    __WOOD_BACKGROUND = "#c38a06"
    __ANIMATION_DELAY_SECONDS = 0.3

    def __init__(self, controls):
        self.__root = tk.Tk()
        self.__root.title("Puzzle")
        self.__root.configure(background=self.__WOOD_BACKGROUND)
        self.__size_dropdown = TkPuzzleDropdown(self.__root, self.__WOOD_BACKGROUND)
        self.__status_bar = TkStatusBar(self.__root, self.__WOOD_BACKGROUND)
        self.__board = TkBoard(self.__root, self.__WOOD_BACKGROUND)
        self.__control_panel = TkControlPanel(self.__root, self.__WOOD_BACKGROUND, controls)

    def bind(self, listener):
        self.__size_dropdown.bind(listener)
        self.__control_panel.bind(listener)
        self.__size_dropdown.announce(listener)

    def rebuild(self, size, listener):
        self.__board.rebuild(size, listener)

    def display(self, row, column, value):
        self.__board.display(row, column, value)

    def animate(self, steps, visitor):
        for step in steps:
            step.accept(visitor)
            self.__refresh()

    def notify(self, text, duration=None):
        self.__status_bar.show(text, duration)

    def run(self):
        self.__root.mainloop()

    def __refresh(self):
        self.__root.update()
        time.sleep(self.__ANIMATION_DELAY_SECONDS)