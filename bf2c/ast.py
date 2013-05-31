class Cmd(object):
    glyph = ''

    def __repr__(self):
        return self.glyph

    def compile(self):
        raise NotImplementedError


class Prog(Cmd, list):
    def compile(self):
        return ''.join(repr(i) for i in self)


class IncP(Cmd):
    glyph = '>'


class DecP(Cmd):
    glyph = '<'


class IncB(Cmd):
    glyph = '+'


class DecB(Cmd):
    glyph = '-'


class Out(Cmd):
    glyph = '.'


class In(Cmd):
    glyph = ','


class JmpF(Cmd):
    glyph = '['


class JmpB(Cmd):
    glyph = ']'
