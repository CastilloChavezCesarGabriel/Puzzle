import tkinter as tk
from tkinter import font
from adapters.tk.tk_board_frame import TkBoardFrame

class TkBoard:
    __TILE_BACKGROUND = "#d8b292"
    __TILE_ACTIVE = "#e6c5a8"
    __TILE_TEXT = "#6b3f12"
    __EMPTY_BACKGROUND = "#2f241a"

    def __init__(self, root, background, size):
        self.__size = size
        self.__frame = TkBoardFrame.create(root, background)
        self.__font = font.Font(family="Helvetica", size=25, weight="bold")
        self.__tiles = self.__populate()
        self.__configure()

    def bind(self, listener):
        for row_index, row in enumerate(self.__tiles):
            for column_index, tile in enumerate(row):
                tile.configure(command=lambda r=row_index, c=column_index: listener.on_click(r, c))

    def display(self, state, size):
        for row_index in range(size):
            for column_index in range(size):
                value = state[row_index * size + column_index]
                self.__render(self.__tiles[row_index][column_index], value)

    @staticmethod
    def __render(tile, value):
        if value == 0:
            tile.config(text="", bg=TkBoard.__EMPTY_BACKGROUND,
                        activebackground=TkBoard.__EMPTY_BACKGROUND, relief="sunken")
        else:
            tile.config(text=str(value), bg=TkBoard.__TILE_BACKGROUND,
                        activebackground=TkBoard.__TILE_ACTIVE)

    def __populate(self):
        tiles = []
        for row_index in range(self.__size):
            row = [self.__place(row_index, column_index) for column_index in range(self.__size)]
            tiles.append(row)
        return tiles

    def __place(self, row, column):
        tile = tk.Button(self.__frame, text="", width=4, height=2, font=self.__font,
            bg=TkBoard.__TILE_BACKGROUND, fg=TkBoard.__TILE_TEXT,
            activebackground=TkBoard.__TILE_ACTIVE, activeforeground=TkBoard.__TILE_TEXT,
            relief="raised", bd=6)
        tile.grid(row=row, column=column, padx=6, pady=6, sticky="nsew")
        return tile

    def __configure(self):
        for index in range(self.__size):
            self.__frame.grid_rowconfigure(index, weight=1)
            self.__frame.grid_columnconfigure(index, weight=1)