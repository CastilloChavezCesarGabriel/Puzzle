from model.cell import Cell
from model.position import Position

class Space:
    def __init__(self, state, size):
        self.__state = state
        self.__size = size
        self.__empty_index = state.index(Cell.EMPTY)

    def expand(self):
        row, column = divmod(self.__empty_index, self.__size)
        neighbors = []
        for axis, step in ((row, self.__size), (column, 1)):
            if axis > 0:
                neighbors.append(self.__empty_index - step)
            if axis < self.__size - 1:
                neighbors.append(self.__empty_index + step)
        return neighbors

    def decode(self, index):
        return Position(*divmod(index, self.__size))

    def swap(self, position):
        if not position.is_adjacent(self.decode(self.__empty_index)):
            return None
        target_index = position.flatten(self.__size)
        new_state = list(self.__state)
        new_state[self.__empty_index], new_state[target_index] = \
            (new_state[target_index], new_state[self.__empty_index],)
        return tuple(new_state)