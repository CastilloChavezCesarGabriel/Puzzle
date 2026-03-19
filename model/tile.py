class Tile:
    def __init__(self, row, column):
        self.__row = row
        self.__column = column

    def move(self, state, size):
        empty_index = state.index(0)
        empty_row, empty_column = divmod(empty_index, size)
        if not self.__is_adjacent(empty_row, empty_column):
            return None
        target_index = self.__row * size + self.__column
        tiles = list(state)
        tiles[empty_index], tiles[target_index] = tiles[target_index], tiles[empty_index]
        return tuple(tiles)

    def __is_adjacent(self, empty_row, empty_column):
        row_distance = abs(empty_row - self.__row)
        column_distance = abs(empty_column - self.__column)
        horizontal_neighbor = row_distance == 0 and column_distance == 1
        vertical_neighbor = row_distance == 1 and column_distance == 0
        return horizontal_neighbor or vertical_neighbor