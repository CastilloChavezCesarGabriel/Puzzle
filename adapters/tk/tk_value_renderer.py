from adapters.tk.tk_renderer import TkRenderer

class TkValueRenderer(TkRenderer):
    __BACKGROUND = "#d8b292"
    __ACTIVE_BACKGROUND = "#e6c5a8"
    __TEXT = "#6b3f12"

    def render(self, tile, value):
        tile.config(text=str(value), bg=self.__BACKGROUND, fg=self.__TEXT,
                    activebackground=self.__ACTIVE_BACKGROUND, activeforeground=self.__TEXT)