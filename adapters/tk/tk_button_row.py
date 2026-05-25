import tkinter as tk

class TkButtonRow:
    def __init__(self, container, controls):
        self.__buttons = controls
        self.__widgets = []
        for column_index in range(len(controls)):
            widget = tk.Button(container, font=("Helvetica", 11), width=10)
            widget.grid(row=0, column=column_index, padx=6)
            self.__widgets.append(widget)

    def bind(self, listener):
        for button, widget in zip(self.__buttons, self.__widgets):
            button.configure(widget, listener)