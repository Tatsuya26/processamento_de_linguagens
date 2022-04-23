import ply.lex as lex

tokens =["NUM","OPERADORES"]

t_NUM = '\d+'
t_OPERADORES = '[+|*|-]'

t_ignore='\n\t '

def t_error(t):
    print("Erro")
    print(t)

lexer = lex.lex()


# 1+2 1-2 1*2
# ola mundo
import sys
for line in sys.stdin:
    lexer.input(line)
    for tok in lexer:
        print(tok)