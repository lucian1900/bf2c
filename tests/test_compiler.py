from bf2c.parser import parse
from bf2c.ast import *


def test_simple():
    assert parse('><[+-.,]').compile() == """
#include <stdlib.h>
int main() {
    int *p = malloc(1024);
    ++p;
    --p;
    while (*p) {
    ++*p;
    --*p;
    putchar(*p);
    *p = getchar();
    free(p);
}
"""
