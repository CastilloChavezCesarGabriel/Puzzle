from controller.puzzle_animation_solver import PuzzleAnimationSolver
from controller.puzzle_mover import PuzzleMover
from controller.puzzle_resetter import PuzzleResetter
from controller.puzzle_shuffler import PuzzleShuffler
from model.puzzle import Puzzle

class PuzzleGame:
    __INITIAL_SIZE = 2

    def __init__(self, policy):
        self.__policy = policy
        self.__puzzle = Puzzle(self.__INITIAL_SIZE)
        self.__solver = policy.create(self.__INITIAL_SIZE)

    def resize(self, size):
        self.__puzzle = Puzzle(size)
        self.__solver = self.__policy.create(size)

    def move(self, position, view, duration):
        mover = PuzzleMover(view, duration)
        new_puzzle = mover.move(self.__puzzle, position)
        if new_puzzle == self.__puzzle:
            return False
        self.__puzzle = new_puzzle
        return True

    def shuffle(self, view, duration):
        shuffler = PuzzleShuffler(view, duration)
        self.__puzzle = shuffler.shuffle(self.__puzzle)

    def reset(self, view, duration):
        resetter = PuzzleResetter(view, duration)
        self.__puzzle = resetter.reset(self.__puzzle)

    def solve(self, view, duration):
        solver = PuzzleAnimationSolver(self.__solver, view)
        self.__puzzle = solver.solve(self.__puzzle, duration)

    def accept(self, visitor):
        self.__puzzle.accept(visitor)