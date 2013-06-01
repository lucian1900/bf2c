class Prog(list):
    def __repr__(self):
        return ''.join(repr(i) for i in self)

    def compile(self):
        raise ''
