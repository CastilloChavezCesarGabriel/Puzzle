class Solution:
    def __init__(self, steps):
        self.__steps = steps

    def __bool__(self):
        return bool(self.__steps)

    def __iter__(self):
        return iter(self.__steps)

    def conclude(self):
        return self.__steps[-1]