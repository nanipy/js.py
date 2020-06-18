import re

from forbiddenfruit import curses


@curses(str, "length")
@property
def length(self):
    return len(self)


@curses(str, "constructor")
@property
def constructor(self):
    return type(self)


@curses(str, "prototype")
@property
def prototype(self):
    # TODO
    raise NotImplementedError("Not possible in Python yet, coming soon")


@curses(str, "charAt")
def charAt(self, index):
    return self[index]


@curses(str, "charCodeAt")
def charCodeAt(self, index):
    return ord(self[index])


@curses(str, "concat")
def concat(self, *strings):
    return f"{self}{''.join(strings)}"


@curses(str, "endsWith")
def endsWith(self, search_string, position=None):
    if position is None or position > len(self):
        position = len(self)
    self = self[:position]
    return self.endswith(search_string)


@curses(str, "fromCharCode")
@classmethod
def fromCharCode(cls, *codes):
    return cls("".join([chr(int(c)) for c in codes]))


@curses(str, "includes")
def includes(self, search_string, position=0):
    if position + len(search_string) > len(self):
        return False
    return search_string in self


@curses(str, "indexOf")
def indexOf(self, item, start=0):
    try:
        return self[start:].index(item)
    except ValueError:  # we want it to be the exact JS way and return -1 if not found
        return -1


@curses(str, "lastIndexOf")
def lastIndexOf(self, item, start=-1):
    try:
        return len(self) - 1 - self[::start].index(item)
    except ValueError:  # we want it to be the exact JS way and return -1 if not found
        return -1


@curses(str, "localeCompare")
def localeCompare(self, compare, locales, options):
    raise NotImplementedError("To be implemented soon")


@curses(str, "match")
def match(self, regexpr):
    return re.findall(regexpr, self)


@curses(str, "repeat")
def repeat(self, times):
    times = round(times)
    if times < 0:
        raise ValueError("Times must be positive or 0!")
    return self * times


@curses(str, "_replace")
def _replace(self, find, replace):
    pass  # one day make this the JS replace supporting regexes, but py replace is fine for now


@curses(str, "search")
def search(self, val):
    return self.index(val)


@curses(str, "slice")
def slice(self, start, end):
    return self[start:end]


@curses(str, "split")
def _split(self, seperator=None, limit=None):
    if seperator is None:
        return list(self)
    return self.split(seperator)[:limit]


@curses(str, "startsWith")
def startsWith(self, search_string, position=None):
    if position is None or position > len(self):
        position = len(self)
    self = self[:position]
    return self.startswith(search_string)


@curses(str, "substr")
def substr(self, start, maxlength):
    return self[start:][:maxlength]


@curses(str, "substring")
def substring(self, start, end=None):
    if end is None or end > len(self):
        end = len(self)
    if start > len(self):
        start = len(self)
    start, end = sorted([start, end])
    return self[start:end]


@curses(str, "toLocaleLowerCase")
def toLocaleLowerCase(self):
    raise NotImplementedError("To be implemented soon")


@curses(str, "toLocaleUpperCase")
def toLocaleUpperCase(self):
    raise NotImplementedError("To be implemented soon")


@curses(str, "toLowerCase")
def toLowerCase(self):
    return self.lower()


@curses(str, "toString")
def toString(self):
    return self


@curses(str, "toUpperCase")
def toUpperCase(self):
    return self.upper()


@curses(str, "trim")
def trim(self):
    return self.strip()


@curses(str, "valueOf")
def valueOf(self):
    return self
