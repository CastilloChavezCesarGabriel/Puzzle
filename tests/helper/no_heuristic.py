from model.heuristic import Heuristic

class NoHeuristic(Heuristic):
    def estimate(self, state):
        return 0