from copy import copy

class Array(list):

    def __getslice__(self, i, j):
        return Array(list.__getslice__(self, i, j))

    def __add__(self, other):
        return Array(list.__add__(self, other))

    def __mul__(self, other):
        return Array(list.__mul__(self, other))

    def __getitem__(self, item):
        result = list.__getitem__(self, item)
        try:
            return Array(result)
        except TypeError:
            return result

    @property
    def constructor(self):
        """Returns the function that created the Array object's prototype"""
        return type(self)

    @property
    def length(self):
        """Returns the current length of the Array"""
        return len(self)

    @length.setter
    def length(self, new_length):
        if new_length < 0:
            raise ArgumentError("New Array length must be positive")
        for i in self[new_length:]:
            self.remove(i)

    @property
    def prototype(self):
        raise NotImplementedError("Not possible in Python yet, coming soon")

    def concat(self, *arrays):
        """Merge the Array with any other Arrays."""
        for arr in arrays:
            self.extend(arr)

    def copyWithin(self, target, start=0, end=None):
        if target < 0:
            target = len(self) + target
        if end is None:
            end = len(self)
        array_to_copy = self[start:end][:len(self) - target]
        tmp = copy(self)
        for i, j in enumerate(array_to_copy):
            tmp[target + i] = j
        return tmp
