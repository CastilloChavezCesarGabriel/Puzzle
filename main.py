from adapters.tk.tk_puzzle_exit_button import TkPuzzleExitButton
from adapters.tk.tk_puzzle_view import TkPuzzleView
from controller.puzzle_controller import PuzzleController
from controller.puzzle_game import PuzzleGame
from model.puzzle_solver_policy import PuzzleSolverPolicy
from view.puzzle_reset_button import PuzzleResetButton
from view.puzzle_shuffle_button import PuzzleShuffleButton
from view.puzzle_solve_button import PuzzleSolveButton

if __name__ == "__main__":
    policy = PuzzleSolverPolicy()
    game = PuzzleGame(policy)
    buttons = [
        PuzzleShuffleButton(),
        PuzzleSolveButton(),
        PuzzleResetButton(),
        TkPuzzleExitButton(),
    ]
    view = TkPuzzleView(buttons)
    controller = PuzzleController(game, view)
    controller.run()
