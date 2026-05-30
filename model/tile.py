from model.position import Position

class Tile:
    def __init__(self, position):
        self.__position = position

    def move(self, state, size):
        empty_index = state.index(0)
        empty_position = Position(*divmod(empty_index, size))
        if not self.__position.is_adjacent(empty_position):
            return None
        target_index = self.__position.flatten(size)
        new_state = list(state)
        new_state[empty_index], new_state[target_index] = new_state[target_index], new_state[empty_index]
        return tuple(new_state)