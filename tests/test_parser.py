from bf2c.parser import parse
from bf2c.ast import *


def test_simple():
    assert parse('') == Prog()
    assert parse('+') == Prog(['+'])
    assert parse('+-') == Prog(['+', '-'])