from model.heuristic_puzzle_solver import HeuristicPuzzleSolver
from model.manhattan_distance_algorithm import ManhattanDistanceAlgorithm
from model.puzzle import Puzzle
from view.puzzle_exit_button import PuzzleExitButton
from view.puzzle_reset_button import PuzzleResetButton
from view.puzzle_shuffle_button import PuzzleShuffleButton
from view.puzzle_solve_button import PuzzleSolveButton
from view.puzzle_view import View
from controller.puzzleController import Controller

if __name__ == "__main__":
    size = 4
    solver = HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(size))

    buttons = [
        PuzzleShuffleButton(),
        PuzzleSolveButton(),
        PuzzleResetButton(),
        PuzzleExitButton(),
    ]

    view = View(size, buttons)
    puzzle = Puzzle(size)
    controller = Controller(solver, view, puzzle)
    controller.run()