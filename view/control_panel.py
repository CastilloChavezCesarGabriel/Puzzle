import tkinter as tk

class ControlPanel:
    __LABELS = ("Shuffle", "Solve", "Reset", "Exit")

    def __init__(self, root, background):
        self.__root = root
        self.__background = background
        self.__buttons = self.__assemble()

    def bind(self, listener):
        commands = [
            lambda: listener.on_shuffle(),
            lambda: listener.on_solve(),
            lambda: listener.on_reset(),
            self.__root.quit,
        ]
        for button, command in zip(self.__buttons, commands):
            button.configure(command=command)

    def __assemble(self):
        container = tk.Frame(self.__root, bg=self.__background)
        container.pack(pady=8)
        buttons = []
        for column_index, text in enumerate(ControlPanel.__LABELS):
            button = tk.Button(container, text=text, font=("Helvetica", 11), width=10)
            button.grid(row=0, column=column_index, padx=6)
            buttons.append(button)
        return buttons