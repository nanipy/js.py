import builtins

from .core import *

# Patch console.log
builtins.console = console
# Patch require
builtins.require = require
