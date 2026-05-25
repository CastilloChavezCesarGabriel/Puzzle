from adapters.tk.tk_puzzle_exit_button import TkPuzzleExitButton
from adapters.tk.tk_puzzle_view import TkPuzzleView
from controller.puzzle_controller import PuzzleController
from model.heuristic_puzzle_solver import HeuristicPuzzleSolver
from model.manhattan_distance_algorithm import ManhattanDistanceAlgorithm
from model.puzzle import Puzzle
from view.puzzle_reset_button import PuzzleResetButton
from view.puzzle_shuffle_button import PuzzleShuffleButton
from view.puzzle_solve_button import PuzzleSolveButton

if __name__ == "__main__":
    size = 4
    manhattan_distance_algorithm = ManhattanDistanceAlgorithm(size)
    solver = HeuristicPuzzleSolver(manhattan_distance_algorithm)

    buttons = [
        PuzzleShuffleButton(),
        PuzzleSolveButton(),
        PuzzleResetButton(),
        TkPuzzleExitButton(),
    ]

    view = TkPuzzleView(size, buttons)
    puzzle = Puzzle(size)
    controller = PuzzleController(solver, view, puzzle)
    controller.run()