from view.puzzle_button import IPuzzleButton

class PuzzleSolveButton(IPuzzleButton):
    def configure(self, widget, listener):
        widget.configure(text="Solve", command=lambda: listener.on_solve())