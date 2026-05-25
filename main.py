from model.heuristic_puzzle_solver import HeuristicPuzzleSolver
from model.manhattan_distance_algorithm import ManhattanDistanceAlgorithm
from model.puzzle import Puzzle
from view.puzzleView import View
from controller.puzzleController import Controller

if __name__ == "__main__":
    size = 4
    solver = HeuristicPuzzleSolver(ManhattanDistanceAlgorithm(size))
    view = View()
    controller = Controller(solver, view, Puzzle(size))
    controller.run()