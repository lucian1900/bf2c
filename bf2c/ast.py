template = """
#include <stdlib.h>
int main() {{
    int *p = malloc(1024);
    {0}
    free(p);
}}
"""

commands = {
    '>': '++p;',
    '<': '--p;',
    '+': '++*p;',
    '-': '--*p;',
    '.': 'putchar(*p);',
    ',': '*p = getchar();',
    '[': 'while (*p) {',
    ']': '}',
}


class Prog(list):
    def __repr__(self):
        return 'Prog(' +  ''.join(i for i in self) + ')'

    def compile(self):
        prog = '\n    '.join(
            commands[i] for i in self
        )
        return template.format(prog)
