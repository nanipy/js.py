import collections
from copy import copy
from inspect import signature

from forbiddenfruit import curse, curses


def issequenceforme(obj):
    if isinstance(obj, str):
        return False
    return isinstance(obj, collections.Sequence)


@curses(list, "from")
@classmethod
def _from(cls, obj, mapfn=None):
    mapfn = mapfn or (lambda x: x)
    return cls(list(map(mapfn, list(obj))))


@curses(list, "constructor")
@property
def constructor(self):
    """Returns the function that created the Array object's prototype"""
    return type(self)


def get_length(self):
    """Returns the current length of the Array"""
    return len(self)


def set_length(self, new_length):
    if new_length < 0:
        raise ValueError("New Array length must be positive")
    for i in self[new_length:]:
        self.remove(i)
    old_len = len(self)
    if new_length > old_len:
        for i in range(
            new_length - old_len
        ):  # allow setting a higher length than currently existing
            self.append(None)


curse(list, "length", property(get_length, set_length))


@curses(list, "prototype")
@property
def prototype(self):
    # TODO: impl setattr via curses?
    raise NotImplementedError("Not possible in Python yet, coming soon")


@curses(list, "concat")
def concat(self, *arrays):
    """Merge the Array with any other Arrays."""
    for arr in arrays:
        self.extend(arr)


@curses(list, "copyWithin")
def copyWithin(self, target, start=0, end=None):
    if target < 0:
        target = len(self) + target
    if end is None:
        end = len(self)
    array_to_copy = self[start:end][: len(self) - target]
    tmp = copy(self)
    for i, j in enumerate(array_to_copy):
        tmp[target + i] = j
    return tmp


@curses(list, "entries")
def entries(self):
    for i, j in enumerate(self):
        yield [i, j]


@curses(list, "every")
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


@curses(list, "forEach")
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


@curses(list, "filter")
def filter(self, callback, this=None):
    self = this or self
    params = signature(callback).parameters
    passed = []
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


@curses(list, "map")
def _map(self, callback, this=None):
    self = this or self
    params = signature(callback).parameters
    res = []
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


@curses(list, "findIndex")
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


@curses(list, "find")
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


@curses(list, "fill")
def fill(self, val, start=0, end=None):
    if end is None or end > len(self):
        end = len(self)
    for i in range(start, end):
        self[i] = val
    return self


@curses(list, "includes")
def includes(self, item, start=0):
    return item in self[start:]


@curses(list, "indexOf")
def indexOf(self, item, start=0):
    try:
        return self[start:].index(item)
    except ValueError:  # we want it to be the exact JS way and return -1 if not found
        return -1


@curses(list, "lastIndexOf")
def lastIndexOf(self, item, start=-1):
    try:
        return len(self) - 1 - self[::start].index(item)
    except ValueError:  # we want it to be the exact JS way and return -1 if not found
        return -1


@curses(list, "push")
def push(self, *items):
    for i in items:
        self.append(i)
    return len(self)


@curses(list, "reduce")
def reduce(self, callback, initial=None):
    params = signature(callback).parameters
    if initial is None:
        ret = self[0]
        idx = 1
    else:
        ret = initial
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


@curses(list, "reduceRight")
def reduceRight(self, callback, initial=None):
    params = signature(callback).parameters
    self_2 = self[::-1]
    if initial is None:
        ret = self_2[0]
        idx = 1
    else:
        ret = initial
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


@curses(list, "reverse")
def reverse(self):
    old = copy(self)
    for i, j in enumerate(old):
        self[-(i + 1)] = j
    return self


@curses(list, "shift")
def shift(self):
    i = self[0]
    del self[0]
    return i


@curses(list, "slice")
def slice(self, start, end):
    return self[start:end]


@curses(list, "some")
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


_old_sort = list.sort


@curses(list, "sort")
def _sort(self, func=None):
    if not func:
        _old_sort(self)
    else:
        _old_sort(self, key=func)


@curses(list, "splice")
def splice(self, index, delete_count=0, *added):
    out = []
    for i in range(delete_count):
        out.append(self[index + i])
        del self[index + i]
    for i, j in enumerate(added):
        self.insert(index + i, j)
    return out


@curses(list, "toString")
def toString(self):
    return ",".join(str(i) for i in self)


@curses(list, "unshift")
def unshift(self, *elements):
    self[0:0] = elements
    return len(self)


@curses(list, "valueOf")
def valueOf(self):
    return self
