from bf2c.ast import *
from bf2c.parser import parse


def test_simple():
    assert parse('') == Prog()
    assert parse('+') == Prog([IncB()])
