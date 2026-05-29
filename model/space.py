class Space:
    def __init__(self, state, size):
        self.__state = state
        self.__size = size

    def expand(self):
        index = self.__state.index(0)
        row, column = divmod(index, self.__size)
        moves = []
        for axis, step in ((row, self.__size), (column, 1)):
            if axis > 0:
                moves.append((index, index - step))
            if axis < self.__size - 1:
                moves.append((index, index + step))
        return moves