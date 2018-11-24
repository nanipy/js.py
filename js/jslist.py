from copy import copy

class JSList(list):
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
        self = self[:new_length]

    @property
    def prototype(self):
        raise NotImplementedError("Not possible in Python yet")

    def concat(self, *arrays):
        """Merge the Array with any other Arrays."""
        for arr in arrays:
            self.extend(arr)

    def copyWithin(self, target, start=0, end=None):
        if target < 0:
            target = len(self) + target
        if end is None:
            end = len(self)
        array_to_copy = self[start:end][:end - target]
        tmp = copy(self)
        for idx, i in enumerate(array_to_copy):
            tmp[target + idx] = i
        return tmp
