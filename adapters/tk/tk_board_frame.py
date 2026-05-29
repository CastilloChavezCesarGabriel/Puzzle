import tkinter as tk

class TkBoardFrame:
    __BOARD_BACKGROUND = "#4b3a27"

    def __init__(self, root, background):
        self.__root = root
        self.__background = background

    def create(self):
        outer = tk.Frame(self.__root, bg=self.__background, bd=18, relief="ridge")
        outer.pack(padx=14, pady=6)
        inner = tk.Frame(outer, bg=self.__BOARD_BACKGROUND, bd=10, relief="sunken")
        inner.pack()
        return inner