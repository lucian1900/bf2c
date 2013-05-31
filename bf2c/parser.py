from functools import wraps

from rply import ParserGenerator

from bf2c.lexer import lexer
from bf2c.ast import *


pg = ParserGenerator(
    [rule.name for rule in lexer.rules],
    cache_id='bf2c',
)


def applied(f):
    @wraps(f)
    def wrapper(args):
        return f(*args)


@pg.production('main : cmds')
def main(p):
    return Prog(p[0])


@pg.production('cmds :')
@pg.production('cmds : cmd')
@pg.production('cmds : cmds cmd')
def cmds(p):
    if len(p) == 0:
        return []

    elif len(p) == 1:
        i = p[0]
        if i is None:
            return []
        return [i]

    elif len(p) == 2:
        lst, i = p
        return lst + [i]

    else:
        lst, _, i = p
        return lst + [i]


@pg.production('cmd : INC_P')
def inc_p(p):
    return IncP(p)


@pg.production('cmd : DEC_P')
def dec_p(p):
    return DecP(p)


@pg.production('cmd : INC_B')
def inc_b(p):
    return IncB(p)


@pg.production('cmd : DEC_B')
def dec_b(p):
    return DecB(p)


@pg.production('cmd : OUT')
def out(p):
    return Out(p)


@pg.production('cmd : IN')
def in_(p):
    return In(p)


@pg.production('cmd : JMP_F')
def jmp_f(p):
    return JmpF(p)


@pg.production('cmd : JMP_B')
def jmp_b(p):
    return JmpB(p)


class SyntaxError(Exception):
    def __init__(self, message, lineno, colno):
        self.message = message
        self.lineno = lineno
        self.colno = colno


@pg.error
def error_handler(token):
    source_pos = token.getsourcepos()
    raise SyntaxError(
        "Got {0} when not expected".format(token.gettokentype()),
        source_pos.lineno,
        source_pos.colno,
    )


parser = pg.build()


def parse(text):
    return parser.parse(lexer.lex(text))
