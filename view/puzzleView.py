import tkinter as tk
from tkinter import font
import time

WOOD_BACKGROUND = "#c38a06"
BOARD_BACKGROUND = "#4b3a27"
TILE_BACKGROUND = "#d8b292"
TILE_ACTIVE = "#e6c5a8"
TILE_TEXT = "#6b3f12"
EMPTY_BACKGROUND = "#2f241a"

class View:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Puzzle")
        self.root.configure(background=WOOD_BACKGROUND)

        self.on_click_tile = None
        self.on_shuffle = None
        self.on_solve = None
        self.on_reset = None

        self.status = tk.StringVar(value="")
        status_font = font.Font(family="Arial", size=20, weight="bold", slant="italic")
        tk.Label(self.root, textvariable=self.status, bg=WOOD_BACKGROUND, fg="white",
                 font=status_font).pack(pady=(6, 10))

        self.frame = self.create_frame()
        self.tiles = self.create_board()
        self.create_controls()

    def create_frame(self):
        outer = tk.Frame(self.root, bg=WOOD_BACKGROUND, bd=18, relief="ridge")
        outer.pack(padx=14, pady=6)
        frame = tk.Frame(outer, bg=BOARD_BACKGROUND, bd=10, relief="sunken")
        frame.pack()
        return frame

    def create_board(self):
        tile_font = font.Font(family="Helvetica", size=25, weight="bold")
        tiles = []
        for i in range(4):
            row = []
            for j in range(4):
                tile = tk.Button(
                    self.frame,
                    text="",
                    width=4,
                    height=2,
                    font=tile_font,
                    bg=TILE_BACKGROUND, fg=TILE_TEXT,
                    activebackground=TILE_ACTIVE,
                    activeforeground=TILE_TEXT,
                    relief="raised",
                    bd=6,
                    command=lambda r=i, c=j: self.on_click_tile and self.on_click_tile(r, c)
                )
                tile.grid(row=i, column=j, padx=6, pady=6, sticky="nsew")
                row.append(tile)
            tiles.append(row)

        for i in range(4):
            self.frame.grid_rowconfigure(i, weight=1)
            self.frame.grid_columnconfigure(i, weight=1)

        return tiles

    def create_controls(self):
        control_frame = tk.Frame(self.root, bg=WOOD_BACKGROUND)
        control_frame.pack(pady=8)

        buttons = [
            ("Shuffle", lambda: self.on_shuffle and self.on_shuffle()),
            ("Solve", lambda: self.on_solve and self.on_solve()),
            ("Reset", lambda: self.on_reset and self.on_reset()),
            ("Exit", self.root.quit),
        ]

        for columns, (text, cmd) in enumerate(buttons):
            tk.Button(control_frame, text=text, command=cmd, font=("Helvetica", 11),
                      width=10).grid(row=0, column=columns, padx=6)

    def display(self, puzzle):
        for i in range(puzzle.size):
            for j in range(puzzle.size):
                value = puzzle.state[i * puzzle.size + j]
                tile = self.tiles[i][j]
                if value == 0:
                    tile.config(text="", bg=EMPTY_BACKGROUND, activebackground=EMPTY_BACKGROUND, relief="sunken")
                else:
                    tile.config(text=str(value), bg=TILE_BACKGROUND, activebackground=TILE_ACTIVE)

    def show_solution(self, steps):
        for step in steps:
            self.display(step)
            self.root.update()
            time.sleep(0.3)

    def show_status(self, text: str):
        self.status.set(text)

    def run(self):
        self.root.mainloop()