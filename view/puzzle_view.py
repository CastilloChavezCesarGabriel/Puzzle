import tkinter as tk
import time

from view.board import Board
from view.control_panel import ControlPanel
from view.status_bar import StatusBar

class View:
    __WOOD_BACKGROUND = "#c38a06"
    __ANIMATION_DELAY_SECONDS = 0.3

    def __init__(self, size):
        self.__root = tk.Tk()
        self.__root.title("Puzzle")
        self.__root.configure(background=View.__WOOD_BACKGROUND)
        self.__status_bar = StatusBar(self.__root, View.__WOOD_BACKGROUND)
        self.__board = Board(self.__root, View.__WOOD_BACKGROUND, size)
        self.__control_panel = ControlPanel(self.__root, View.__WOOD_BACKGROUND)

    def bind(self, listener):
        self.__board.bind(listener)
        self.__control_panel.bind(listener)

    def display(self, state, size):
        self.__board.display(state, size)

    def animate(self, steps, visitor):
        for step in steps:
            step.accept(visitor)
            self.__root.update()
            time.sleep(View.__ANIMATION_DELAY_SECONDS)

    def notify(self, text, duration=None):
        self.__status_bar.show(text, duration)

    def run(self):
        self.__root.mainloop()