from collections.abc import Iterable
from itertools import cycle


class CyclicIterator:

    def __init__(self, iter_obj):
        if isinstance(iter_obj, Iterable):
            self.iter_obj = iter_obj
        else:
            raise ValueError('iter_obj mast be iterable')
        self.__iter = cycle(self.iter_obj)

    def __iter__(self):
        return self

    def __next__(self):
        next_item = next(self.__iter)
        return next_item if type(self.iter_obj) is not dict else self.iter_obj[next_item]

