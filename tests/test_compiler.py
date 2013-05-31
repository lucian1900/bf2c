from pytest import raises

from bf2c.ast import *
from bf2c.compiler import compile
from bf2c.parser import parse


def test_simple():
    fn = Fn(
        Id('main'),
        [],
        Id('int'),
        Block([], None),
    )
    assert compile(fn) == 'int main() {}'


def test_hello():
    fn = Fn(
        Id('main'),
        [],
        Id('int'),
        Block([
            Stmt(Call(Id('print'), [Number(1)])),
        ], None),
    )
    assert compile(fn) == 'int main() {printf("%d", 1); }'


def test_missing():
    ns = parse('''
    fn foo() {
        bar()
    }
    fn baz() {}
    ''')

    with raises(ReferenceError):
        compile(ns)

    ns = parse('''
    fn foo() {
        bar()
    }
    fn bar() {}
    ''')

    assert compile(ns) == 'void foo() {bar()}\nvoid bar() {}'
