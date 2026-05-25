from view.puzzle_button import IPuzzleButton

class TkPuzzleExitButton(IPuzzleButton):
    def configure(self, widget, listener):
        widget.configure(text="Exit", command=widget.winfo_toplevel().quit)