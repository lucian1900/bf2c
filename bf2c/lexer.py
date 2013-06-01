from rply import LexerGenerator

lg = LexerGenerator()

lg.add('INC_P', r'>')
lg.add('DEC_P', r'<')
lg.add('INC_B', r'\+')
lg.add('DEC_B', r'-')
lg.add('OUT',   r'\.')
lg.add('IN',    r',')
lg.add('JMP_F', r'\[')
lg.add('JMP_B', r'\]')

# Everything else is whitespace
lg.ignore(r'[^.><\+-\.,\[\]]')

lexer = lg.build()


def lex(text):
    stream = lexer.lex(text)

    tok = stream.next()
    while tok is not None:
        yield tok
        tok = stream.next()
