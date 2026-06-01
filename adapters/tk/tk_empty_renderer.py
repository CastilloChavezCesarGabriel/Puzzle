from adapters.tk.tk_renderer import TkRenderer

class TkEmptyRenderer(TkRenderer):
    __BACKGROUND = "#2f241a"

    def render(self, tile, value):
        tile.config(text="", bg=self.__BACKGROUND, activebackground=self.__BACKGROUND, relief="sunken")