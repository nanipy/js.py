class Boolean:
    def __init__(self, ex):
        self.internal = ex

    def __repr__(self):
        return str(self.internal).lower()

    def __bool__(self):
        return self.internal # make it behave like a normal boolean
