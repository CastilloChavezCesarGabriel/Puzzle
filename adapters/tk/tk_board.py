import tkinter as tk
from tkinter import font
from adapters.tk.tk_board_frame import TkBoardFrame

class TkBoard:
    __TILE_BACKGROUND = "#d8b292"
    __TILE_ACTIVE = "#e6c5a8"
    __TILE_TEXT = "#6b3f12"
    __EMPTY_BACKGROUND = "#2f241a"

    def __init__(self, root, background):
        self.__frame = TkBoardFrame(root, background).create()
        self.__font = font.Font(family="Helvetica", size=25, weight="bold")
        self.__tiles = {}

    def bind(self, listener):
        for (row, column), tile in self.__tiles.items():
            tile.configure(command=lambda r=row, c=column: listener.on_click(r, c))

    def display(self, row, column, value):
        key = (row, column)
        if key not in self.__tiles:
            self.__tiles[key] = self.__place(row, column)
        self.__render(self.__tiles[key], value)

    def __render(self, tile, value):
        if value == 0:
            tile.config(text="", bg=self.__EMPTY_BACKGROUND,
                        activebackground=self.__EMPTY_BACKGROUND, relief="sunken")
        else:
            tile.config(text=str(value), bg=self.__TILE_BACKGROUND,
                        activebackground=self.__TILE_ACTIVE)

    def __place(self, row, column):
        tile = tk.Button(self.__frame, text="", width=4, height=2, font=self.__font,
            bg=self.__TILE_BACKGROUND, fg=self.__TILE_TEXT,
            activebackground=self.__TILE_ACTIVE, activeforeground=self.__TILE_TEXT,
            relief="raised", bd=6)
        tile.grid(row=row, column=column, padx=6, pady=6, sticky="nsew")
        self.__frame.grid_rowconfigure(row, weight=1)
        self.__frame.grid_columnconfigure(column, weight=1)
        return tile