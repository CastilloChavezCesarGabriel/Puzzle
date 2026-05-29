import tkinter as tk
from tkinter import font
from adapters.tk.tk_board_frame import TkBoardFrame
from shared.position import Position

class TkBoard:
    __TILE_BACKGROUND = "#d8b292"
    __TILE_ACTIVE = "#e6c5a8"
    __TILE_TEXT = "#6b3f12"
    __EMPTY_BACKGROUND = "#2f241a"

    def __init__(self, root, background, size):
        self.__size = size
        self.__frame = TkBoardFrame(root, background).create()
        self.__font = font.Font(family="Helvetica", size=25, weight="bold")
        self.__tiles = self.__populate()
        self.__configure()

    def bind(self, listener):
        for position, tile in self.__tiles.items():
            tile.configure(command=lambda p=position: listener.on_click(p))

    def display(self, position, value):
        self.__render(self.__tiles[position], value)

    def __render(self, tile, value):
        if value == 0:
            tile.config(text="", bg=self.__EMPTY_BACKGROUND,
                        activebackground=self.__EMPTY_BACKGROUND, relief="sunken")
        else:
            tile.config(text=str(value), bg=self.__TILE_BACKGROUND,
                        activebackground=self.__TILE_ACTIVE)

    def __populate(self):
        tiles = {}
        for row in range(self.__size):
            for column in range(self.__size):
                tiles[Position(row, column)] = self.__place(row, column)
        return tiles

    def __place(self, row, column):
        tile = tk.Button(self.__frame, text="", width=4, height=2, font=self.__font,
            bg=self.__TILE_BACKGROUND, fg=self.__TILE_TEXT,
            activebackground=self.__TILE_ACTIVE, activeforeground=self.__TILE_TEXT,
            relief="raised", bd=6)
        tile.grid(row=row, column=column, padx=6, pady=6, sticky="nsew")
        return tile

    def __configure(self):
        for index in range(self.__size):
            self.__frame.grid_rowconfigure(index, weight=1)
            self.__frame.grid_columnconfigure(index, weight=1)