from view.puzzle_button import IPuzzleButton

class PuzzleShuffleButton(IPuzzleButton):
    def configure(self, widget, listener):
        widget.configure(text="Shuffle", command=lambda: listener.on_shuffle())