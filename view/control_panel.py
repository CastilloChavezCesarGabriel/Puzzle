import tkinter as tk

from view.button_row import ButtonRow

class ControlPanel:
    def __init__(self, root, background, controls):
        container = tk.Frame(root, bg=background)
        container.pack(pady=8)
        self.__row = ButtonRow(container, controls)

    def bind(self, listener):
        self.__row.bind(listener)