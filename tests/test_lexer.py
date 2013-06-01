from bf2c.lexer import lex


def tokens(text):
    return [t.value for t in lex(text)]


def test_empty():
    assert tokens('') == []
    assert tokens('hello world!') == []


def test_simple():
    assert tokens('+') == ['+']
    assert tokens('+->[,.<]') == ['+', '-', '>', '[', ',', '.', '<', ']']
    assert tokens('++ hello - ') == ['+', '+', '-']
