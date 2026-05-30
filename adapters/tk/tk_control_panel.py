import tkinter as tk

class TkControlPanel:
    def __init__(self, root, background, controls):
        container = tk.Frame(root, bg=background)
        container.pack(pady=8)
        self.__controls = controls
        self.__widgets = []
        for column_index, _ in enumerate(controls):
            widget = tk.Button(container, font=("Helvetica", 11), width=10)
            widget.grid(row=0, column=column_index, padx=6)
            self.__widgets.append(widget)

    def bind(self, listener):
        for control, widget in zip(self.__controls, self.__widgets):
            control.configure(widget, listener)