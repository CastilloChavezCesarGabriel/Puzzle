import tkinter as tk
from tkinter import font
from adapters.tk.tk_board_frame import TkBoardFrame
from adapters.tk.tk_empty_renderer import TkEmptyRenderer
from adapters.tk.tk_value_renderer import TkValueRenderer

class TkBoard:
    def __init__(self, root, background):
        self.__frame = TkBoardFrame(root, background).create()
        self.__font = font.Font(family="Helvetica", size=25, weight="bold")
        self.__tiles = {}
        self.__value_renderer = TkValueRenderer()
        self.__renderers = {0: TkEmptyRenderer()}

    def rebuild(self, size, listener):
        self.__clear()
        self.__build(size, listener)

    def display(self, row, column, value):
        renderer = self.__renderers.get(value, self.__value_renderer)
        renderer.render(self.__tiles[(row, column)], value)

    def __clear(self):
        for tile in self.__tiles.values():
            tile.destroy()
        self.__tiles.clear()

    def __build(self, size, listener):
        for row in range(size):
            for column in range(size):
                tile = self.__place(row, column)
                tile.configure(command=lambda r=row, c=column: listener.on_click(r, c))
                self.__tiles[(row, column)] = tile

    def __place(self, row, column):
        tile = tk.Button(self.__frame, width=4, height=2, font=self.__font, bd=6)
        tile.grid(row=row, column=column, padx=6, pady=6, sticky="nsew")
        self.__frame.grid_rowconfigure(row, weight=1)
        self.__frame.grid_columnconfigure(column, weight=1)
        self.__value_renderer.render(tile, "")
        return tile