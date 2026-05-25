import tkinter as tk
from adapters.tk.tk_button_row import TkButtonRow

class TkControlPanel:
    def __init__(self, root, background, controls):
        container = tk.Frame(root, bg=background)
        container.pack(pady=8)
        self.__row = TkButtonRow(container, controls)

    def bind(self, listener):
        self.__row.bind(listener)