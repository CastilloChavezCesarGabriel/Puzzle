from view.puzzle_button import IPuzzleButton

class PuzzleResetButton(IPuzzleButton):
    def configure(self, widget, listener):
        widget.configure(text="Reset", command=lambda: listener.on_reset())