import re
from .array import Array

class String(str):

    def __getslice__(self, i, j):
        return String(str.__getslice__(self, i, j))

    def __add__(self, other):
        return String(str.__add__(self, other))

    def __mul__(self, other):
        return String(str.__mul__(self, other))

    def __getitem__(self, item):
        return str.__getitem__(self, item)

    @property
    def length(self):
        return len(self)

    @property
    def constructor(self):
        return type(self)

    @property
    def prototype(self):
        raise NotImplementedError("Not possible in Python yet, coming soon")

    def charAt(self, index):
        return self[index]

    def charCodeAt(self, index):
        return ord(self[index])

    def concat(self, *strings):
        return String(f"{self}{''.join(strings)}")

    def endsWith(self, search_string, position=None):
        if position is None or position > len(self):
            position = len(self)
        self = self[:position]
        return self.endswith(search_string)

    @classmethod
    def fromCharCode(cls, *codes):
        return cls(''.join([chr(int(c)) for c in codes]))

    def includes(self, search_string, position=0):
        if position + len(search_string) > len(self):
            return False
        return search_string in self

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

    def localeCompare(self, compare, locales, options):
        raise NotImplementedError("To be implemented soon")

    def match(self, regexpr):
        return re.findall(regexpr, self)

    def repeat(self, times):
        times = round(times)
        if times < 0:
            raise ValueError("Times must be positive or 0!")
        return self * times

    def _replace(self, find, replace):
        pass # one day make this the JS replace supporting regexes, but py replace is fine for now

    def search(self, val):
        return self.index(val)

    def slice(self, start, end):
        return self[start:end]

    def _split(self, seperator=None, limit=None):
        if seperator is None:
            return Array([self])
        return Array(self.split(seperator))[:limit]

    def startsWith(self, search_string, position=None):
        if position is None or position > len(self):
            position = len(self)
        self = self[:position]
        return self.startswith(search_string)

    def substr(self, start, maxlength):
        return self[start:][:maxlength]

    def substring(self, start, end=None):
        if end is None or end > len(self):
            end = len(self)
        if start > len(self):
            start = len(self)
        start, end = sorted([start, end])
        return self[start:end]

    def toLocaleLowerCase(self):
        raise NotImplementedError("To be implemented soon")

    def toLocaleUpperCase(self):
        raise NotImplementedError("To be implemented soon")

    def toLowerCase(self):
        return self.lower()

    def toString(self):
        return self

    def toUpperCase(self):
        return self.upper()

    def trim(self):
        return self.strip()

    def valueOf(self):
        return self
