import tkinter as tk

class TkBoardFrame:
    __BOARD_BACKGROUND = "#4b3a27"

    @staticmethod
    def create(root, background):
        outer = tk.Frame(root, bg=background, bd=18, relief="ridge")
        outer.pack(padx=14, pady=6)
        inner = tk.Frame(outer, bg=TkBoardFrame.__BOARD_BACKGROUND, bd=10, relief="sunken")
        inner.pack()
        return inner