import tkinter as tk

class ControlPanel:
    def __init__(self, root, background):
        self.__listener = None
        self.__root = root
        self.__background = background
        self.__build()

    def add(self, listener):
        self.__listener = listener

    def __build(self):
        container = tk.Frame(self.__root, bg=self.__background)
        container.pack(pady=8)

        buttons = [
            ("Shuffle", lambda: self.__listener and self.__listener.on_shuffle()),
            ("Solve", lambda: self.__listener and self.__listener.on_solve()),
            ("Reset", lambda: self.__listener and self.__listener.on_reset()),
            ("Exit", self.__root.quit),
        ]

        for column_index, (text, command) in enumerate(buttons):
            tk.Button(container, text=text, command=command, font=("Helvetica", 11),
                      width=10).grid(row=0, column=column_index, padx=6)