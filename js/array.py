from copy import copy
from inspect import signature
import collections

def issequenceforme(obj):
    if isinstance(obj, str):
        return False
    return isinstance(obj, collections.Sequence)

class Array(list):

    def __getslice__(self, i, j):
        return Array(list.__getslice__(self, i, j))

    def __add__(self, other):
        return Array(list.__add__(self, other))

    def __mul__(self, other):
        return Array(list.__mul__(self, other))

    def __getitem__(self, item):
        result = list.__getitem__(self, item)
        if issequenceforme(result):
            return Array(result)
        else:
            return result

    @classmethod
    def _from(cls, obj, mapfn=None):
        mapfn = mapfn or (lambda x: x)
        return cls(list(map(mapfn, list(obj))))

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

    def entries(self):
        for i, j in enumerate(self):
            yield Array([i, j])

    def every(self, callback, this=None):
        self = this or self
        params = signature(callback).parameters
        if len(params) == 1:
            for i in self:
                if callback(i) is False:
                    return False
        elif len(params) == 2:
            for i, j in enumerate(self):
                if callback(j, i) is False:
                    return False
        elif len(params) == 3:
            for i, j in enumerate(self):
                if callback(j, i, self) is False:
                    return False
        return True

    def forEach(self, callback, this=None):
        self = this or self
        params = signature(callback).parameters
        if len(params) == 1:
            for i in self:
                callback(i)
        elif len(params) == 2:
            for i, j in enumerate(self):
                callback(j, i)
        elif len(params) == 3:
            for i, j in enumerate(self):
                callback(j, i, self)

    def filter(self, callback, this=None):
        self = this or self
        params = signature(callback).parameters
        passed = Array()
        if len(params) == 1:
            for i in self:
                if callback(i) is True:
                    passed.append(i)
        elif len(params) == 2:
            for i, j in enumerate(self):
                if callback(j, i) is True:
                    passed.append(j)
        elif len(params) == 3:
            for i, j in enumerate(self):
                if callback(j, i, self) is True:
                    passed.append(j)
        return passed

    def _map(self, callback, this=None):
        self = this or self
        params = signature(callback).parameters
        res = Array()
        if len(params) == 1:
            for i in self:
                res.append(callback(i))
        elif len(params) == 2:
            for i, j in enumerate(self):
                res.append(callback(j, i))
        elif len(params) == 3:
            for i, j in enumerate(self):
                res.append(callback(j, i, self))
        return res

    def findIndex(self, callback, this=None):
        self = this or self
        params = signature(callback).parameters
        if len(params) == 1:
            for i, j in enumerate(self):
                if callback(j) is True:
                    return i
        elif len(params) == 2:
            for i, j in enumerate(self):
                if callback(j, i) is True:
                    return i
        elif len(params) == 3:
            for i, j in enumerate(self):
                if callback(j, i, self) is True:
                    return i
        return None

    def find(self, callback, this=None):
        self = this or self
        params = signature(callback).parameters
        if len(params) == 1:
            for i in self:
                if callback(i) is True:
                    return i
        elif len(params) == 2:
            for i, j in enumerate(self):
                if callback(j, i) is True:
                    return j
        elif len(params) == 3:
            for i, j in enumerate(self):
                if callback(j, i, self) is True:
                    return j
        return None

    def fill(self, val, start=0, end=None):
        if end is None or end > len(self):
            end = len(self)
        for i in range(start, end):
            self[i] = val
        return self

    def includes(self, item, start=0):
        return item in self[start:]

    def indexOf(self, item, start=0):
        try:
            return self[start:].index(item)
        except ValueError: # we want it to be the exact JS way and return -1 if not found
            return -1

    def lastIndexOf(self, item, start=-1):
        try:
            return len(self) - 1 - self[::start].index(item)
        except ValueError: # we want it to be the exact JS way and return -1 if not found
            return -1

    def push(self, *items):
        for i in items:
            self.append(i)
        return len(self)

    def reduce(self, callback, initial=None):
        params = signature(callback).parameters
        if initial is None:
            ret = self[0]
            idx = 1
        else:
            ret = inital
            idx = 0
        while idx < len(self):
            if len(params) == 2:
                ret = callback(ret, self[idx])
            elif len(params) == 3:
                ret = callback(ret, self[idx], idx)
            elif len(params) == 4:
                ret = callback(ret, self[idx], idx, self)
            idx += 1
        return ret

    def reduceRight(self, callback, initial=None):
        params = signature(callback).parameters
        self_2 = self[::-1]
        if initial is None:
            ret = self_2[0]
            idx = 1
        else:
            ret = inital
            idx = 0
        while idx < len(self_2):
            if len(params) == 2:
                ret = callback(ret, self_2[idx])
            elif len(params) == 3:
                ret = callback(ret, self_2[idx], idx)
            elif len(params) == 4:
                ret = callback(ret, self_2[idx], idx, self)
            idx += 1
        return ret

    def reverse(self):
        old = copy(self)
        for i, j in enumerate(old):
            self[-(i + 1)] = j
        return self

    def shift(self):
        i = self[0]
        del self[0]
        return i

    def slice(self, start, end):
        return self[start:end]

    def some(self, callback, this=None):
        self = this or self
        params = signature(callback).parameters
        if len(params) == 1:
            for i in self:
                if callback(i) is True:
                    return True
        elif len(params) == 2:
            for i, j in enumerate(self):
                if callback(j, i) is True:
                    return True
        elif len(params) == 3:
            for i, j in enumerate(self):
                if callback(j, i, self) is True:
                    return True
        return False

    def _sort(self, func=None):
        if not func:
            self.sort()
        else:
            self.sort(key=func)

    def splice(self, index, delete_count=0, *added):
        out = Array()
        for i in range(delete_count):
            out.append(self[index + i])
            del self[index + i]
        for i, j in enumerate(added):
            self.insert(index + i, j)
        return out

    def toString(self):
        return ",".join(str(i) for i in self)

    def unshift(self, *elements):
        self[0:0] = elements
        return len(self)

    def valueOf(self):
        return self
