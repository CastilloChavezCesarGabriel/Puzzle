import tkinter as tk
from tkinter import font

class TkStatusBar:
    def __init__(self, root, background):
        self.__root = root
        self.__status = tk.StringVar(value="")
        self.__pending = None
        status_font = font.Font(family="Arial", size=20, weight="bold", slant="italic")
        tk.Label(root, textvariable=self.__status, bg=background,
                 fg="white", font=status_font).pack(pady=(6, 10))

    def show(self, text, duration=None):
        self.__cancel()
        self.__status.set(text)
        if duration is not None:
            self.__schedule(duration)

    def clear(self):
        self.__status.set("")
        self.__pending = None

    def __cancel(self):
        if self.__pending is not None:
            self.__root.after_cancel(self.__pending)
            self.__pending = None

    def __schedule(self, duration):
        self.__pending = self.__root.after(duration, self.clear)