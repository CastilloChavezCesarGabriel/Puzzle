from model.puzzle_cell_visitor import IPuzzleCellVisitor

class CellDisplayVisitor(IPuzzleCellVisitor):
    def __init__(self, view):
        self.__view = view

    def visit(self, row, column, value):
        self.__view.display(row, column, value)