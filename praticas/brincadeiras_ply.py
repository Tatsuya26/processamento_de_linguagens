import ply.lex as lex
import sys

tokens = [
    "PA",
    "PF",
    "NUM",
    "ID",
    "OP"
]


#PLY procura primeiro funções e por ordem

def t_PA(t):
    r'\('
    return t

def t_PF(t):
    r'\)'
    return t

def t_NUM(t):
    r'\d+'
    return t

def t_ID(t):
    r'[_A-Za-z]\w'
    return t

def t_OP(t):
    r'[+*\-/]'
    return t

t_ignore = '\n\t '

def t_error(t):
    print("ERROR: Ilegal character")
    t.lexer.skip(1)

#analisador lexico
lexer = lex.lex()

for line in sys.stdin:
    lexer.input(line)
    for tok in lexer:
        print(tok)