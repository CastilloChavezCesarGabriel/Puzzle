class Space:
    @staticmethod
    def expand(state, size):
        index = state.index(0)
        row, column = divmod(index, size)
        pairs = []
        if row > 0:
            pairs.append((index, index - size))
        if row < size - 1:
            pairs.append((index, index + size))
        if column > 0:
            pairs.append((index, index - 1))
        if column < size - 1:
            pairs.append((index, index + 1))
        return pairs