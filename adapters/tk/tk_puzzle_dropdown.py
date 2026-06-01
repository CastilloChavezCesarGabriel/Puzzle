import tkinter as tk

class TkPuzzleDropdown:
    __SIZES = (2, 3, 4, 5)

    def __init__(self, root, background):
        self.__variable = tk.IntVar(value=self.__SIZES[0])
        menu = tk.OptionMenu(root, self.__variable, *self.__SIZES)
        menu.configure(bg=background)
        menu.pack(pady=4)

    def bind(self, listener):
        self.__variable.trace_add("write", lambda *_: listener.on_change(self.__variable.get()))

    def announce(self, listener):
        listener.on_change(self.__variable.get())