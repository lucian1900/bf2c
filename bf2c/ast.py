class Cmd(object):
    pass


class Prog(Cmd, list):
    pass


class IncP(Cmd):
    pass


class DecP(Cmd):
    pass


class IncB(Cmd):
    pass


class DecB(Cmd):
    pass


class Out(Cmd):
    pass


class In(Cmd):
    pass


class JmpF(Cmd):
    pass


class JmpB(Cmd):
    pass
