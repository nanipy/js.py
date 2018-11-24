from importlib import import_module

def require(module):
    return import_module(module)

def easy_require(module):
    end = module.split(".")[-1]
    globals()[end] = import_module(module)
