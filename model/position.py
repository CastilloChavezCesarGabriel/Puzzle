class Position:
    def __init__(self, row, column):
        self.__row = row
        self.__column = column

    def flatten(self, size):
        return self.__row * size + self.__column

    def is_adjacent(self, other):
        row_distance = abs(self.__row - other.__row)
        column_distance = abs(self.__column - other.__column)
        return (row_distance == 0 and column_distance == 1) or (row_distance == 1 and column_distance == 0)

    def __eq__(self, other):
        return isinstance(other, Position) and self.__row == other.__row and self.__column == other.__column

    def __hash__(self):
        return hash((self.__row, self.__column))
